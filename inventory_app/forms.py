# inventory_app/forms.py
from django import forms
from .models import InventoryMovement

class InventoryMovementForm(forms.ModelForm):
    class Meta:
        model = InventoryMovement
        fields = ["item", "quantity", "source_warehouse", "target_warehouse", "notes"]
        widgets = {
            "item": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "source_warehouse": forms.Select(attrs={"class": "form-control"}),
            "target_warehouse": forms.Select(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"rows": 2, "class": "form-control"}),
        }
