### Installation

### 1. Clone the repository

bash

git clone https://github.com/your-username/inventory-tracker.git
cd inventory-tracker

###2. Create a virtual environment

bash

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

###3. Install dependencies

pip install -r requirements.txt

###4. Run migrations

python manage.py makemigrations
python manage.py migrate

###5. Create a superuser (for admin access)

python manage.py createsuperuser

###6. Run the development server

python manage.py runserver

Project Structure

inventory_tracker/

├── inventory/            # Django app
│   ├── migrations/
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, JS, images
│   ├── models.py         # Models for Warehouse, Item, InventoryMovement
│   ├── views.py          # Views & logic
│   ├── forms.py          # Forms for adding/editing data
│   └── consumers.py      # WebSocket consumers for real-time updates
│
├── inventory_tracker/    # Project settings
├── manage.py
└── requirements.txt
<img width="1920" height="1080" alt="Tracking_Screenshot" src="https://github.com/user-attachments/assets/7ac8a676-748a-4c95-95a7-d6a48b763800" />
<img width="1920" height="1080" alt="Stock_Screenshot" src="https://github.com/user-attachments/assets/e399eeea-46cc-4be5-bea9-4a7475effcdd" />
<img width="1920" height="1080" alt="Notification_Screenshot" src="https://github.com/user-attachments/assets/fb0d88ea-796f-491f-b670-9aaa5727799d" />
<img width="1920" height="1080" alt="Inventory_Screenshot" src="https://github.com/user-attachments/assets/7f6ca75a-7f61-4593-b4cf-54112b4b5023" />





