markdown
# Furniture Shop Ecommerce (Django)

![Project Banner Image](![image](https://github.com/user-attachments/assets/c1e36cb3-b32d-402b-a2b2-446a8acee2ec)
)  
*Add a catchy banner or screenshot of your homepage here*

---

## Table of Contents
- [About](#about)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Models Diagram](#models-diagram)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Screenshots](#screenshots)  
- [Contributing](#contributing)  
- [License](#license)  

---

## About

Furniture Shop is a Django-based ecommerce website for buying elegant, quality furniture.  
This project showcases product listing, categories, user account management, and cart functionality — all built with Django and Tailwind CSS.

> **Credit:** This project was inspired by and built following tutorials from [Code With Steins](https://www.youtube.com/@CodeWithStein).

While still a work in progress, it demonstrates key ecommerce concepts and a clean, responsive design.

---

## Features

- **Product Catalog**: Browse furniture by categories with search functionality
- **User Accounts**: Registration, login, and profile management
- **Shopping Cart**: Add/remove items with dynamic updates using HTMX
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS
- **Admin Dashboard**: Full CRUD operations for products/categories
- **Image Processing**: Automatic thumbnail generation with Pillow
- **Order Management**: View order history and status

---

## Tech Stack

### Core
- **Python 3.10+**
- **Django 4.2**
- **SQLite** (Development - easily swappable for PostgreSQL)

### Frontend
- **Tailwind CSS** (Styling)
- **HTMX** (Dynamic cart interactions)
- **Django Templating Engine**

### Additional Packages
- **Pillow** (Image processing)
- **Django Crispy Forms** (Form rendering)
- **Django Debug Toolbar** (Development)

---

## Models Diagram

![Database Schema](path/to/models-diagram.png)  
*Replace with your generated ER diagram*

Key Models:
```python
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
Installation
Prerequisites
Python 3.10+

pip package manager

Virtual environment (recommended)

Setup Steps
Clone the repository:

bash
git clone https://github.com/yourusername/furniture-shop.git
cd furniture-shop
Create and activate virtual environment:

bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Configure environment variables:
Create .env file in project root with:

ini
SECRET_KEY=your_django_secret_key
DEBUG=True
Apply database migrations:

bash
python manage.py migrate
Create admin user:

bash
python manage.py createsuperuser
Run development server:

bash
python manage.py runserver
Access the application:

Shop: http://localhost:8000/

Admin: http://localhost:8000/admin/

Usage
Customer Flow
Browse Products: Use category filters or search bar

View Details: Click on any product for full details

Add to Cart: Items update dynamically using HTMX

Checkout: Proceed through cart to place order

Track Orders: View order history in user profile

Admin Operations
Access /admin with superuser credentials

Manage:

Products (add/edit/remove)

Categories

Orders

Users

Generate thumbnails automatically when adding product images

Customization
Update Tailwind styles in static/css/styles.css

Modify templates in templates/ directory

Add new product fields in products/models.py

Screenshots
Feature	Preview Image
Homepage	path/to/homepage.png
Product Detail	path/to/detail.png
Shopping Cart	path/to/cart.png
Admin Dashboard	path/to/admin.png
Replace paths with actual screenshot files

Contributing
Contributions are welcome! Here's how to contribute:

Fork the repository

Create your feature branch:

bash
git checkout -b feature/new-feature
Commit your changes:

bash
git commit -m 'Add new feature'
Push to the branch:

bash
git push origin feature/new-feature
Open a pull request

Development Tips:

Run tests with python manage.py test

Format code with Black: black .

Check migrations with python manage.py makemigrations --dry-run

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to Code With Steins for the excellent Django tutorials that inspired this project.
