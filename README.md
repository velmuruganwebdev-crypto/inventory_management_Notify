## Installation

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
│
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
