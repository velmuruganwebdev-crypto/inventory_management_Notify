# inventory_app/views.py
from django.shortcuts import render, redirect
from .forms import InventoryMovementForm
from .models import Warehouse, Item, InventoryMovement
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def add_movement(request):
    if request.method == "POST":
        form = InventoryMovementForm(request.POST)
        if form.is_valid():
            movement = form.save(commit=False)  # don't save yet

            # -------------------------------
            # Validate source warehouse stock
            # -------------------------------
            if movement.source_warehouse:
                movements = InventoryMovement.objects.filter(
                    source_warehouse=movement.source_warehouse
                ) | InventoryMovement.objects.filter(
                    target_warehouse=movement.source_warehouse
                )
                stock_dict = {}
                for m in movements:
                    item_name = m.item.name
                    qty = stock_dict.get(item_name, 0)
                    if m.target_warehouse == movement.source_warehouse:
                        qty += m.quantity
                    if m.source_warehouse == movement.source_warehouse:
                        qty -= m.quantity
                    stock_dict[item_name] = qty

                current_stock = stock_dict.get(movement.item.name, 0)
                if movement.quantity > current_stock:
                    # Not enough stock in source
                    form.add_error(
                        'quantity',
                        f"Not enough {movement.item.name} in {movement.source_warehouse.name}. Available: {current_stock}"
                    )
                    return render(request, "add_movement.html", {"form": form})

            # Save movement
            movement.save()

            # -------------------------------
            # Real-time notification (safe)
            # -------------------------------
            channel_layer = get_channel_layer()
            if channel_layer:
                try:
                    async_to_sync(channel_layer.group_send)(
                        "inventory",
                        {
                            "type": "send_notification",
                            "message": f"{movement.item.name} moved successfully!"
                        }
                    )
                except Exception:
                    pass  # fail-safe

            return redirect("/inventory/add/?success=1&item=" + movement.item.name)

    else:
        form = InventoryMovementForm()
    return render(request, "add_movement.html", {"form": form})


def movement_list(request):
    movements = InventoryMovement.objects.all().order_by('-timestamp')
    return render(request, "movement_list.html", {"movements": movements})


def stock_summary(request):
    summary = []
    warehouses = Warehouse.objects.all()

    for w in warehouses:
        movements = InventoryMovement.objects.filter(
            source_warehouse=w
        ) | InventoryMovement.objects.filter(
            target_warehouse=w
        )
        stock_dict = {}
        for m in movements:
            item_name = m.item.name
            qty = stock_dict.get(item_name, 0)
            if m.target_warehouse == w:
                qty += m.quantity
            if m.source_warehouse == w:
                qty -= m.quantity
            stock_dict[item_name] = qty

        # Only show positive stock
        stock_list = [{'item': k, 'quantity': max(0, v)} for k, v in stock_dict.items()]
        summary.append({
            'warehouse': w.name,
            'stock': stock_list
        })

    return render(request, 'stock_summary.html', {'summary': summary})
