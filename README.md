markdown
# Furniture Shop Ecommerce (Django)

![Product Images](screenshots/image-2.png)

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

**Furniture Shop** is a Django-based ecommerce web application for selling elegant, quality furniture.

While still a work in progress, this project demonstrates key ecommerce concepts and a clean, modern design that’s fully responsive across devices.
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

### 📌 Credits

This project was inspired by and built while following the excellent Django ecommerce tutorials from  
[**Code With Stein**](https://www.youtube.com/@CodeWithStein).  
Much appreciation for those resources!

---

## Tech Stack

### Core
- **Python 3.13.2**
- **Django 5.2.1**
- **SQLite** (Development - easily swappable for PostgreSQL)

### Frontend
- **Tailwind CSS** (Styling)
- **HTMX** (Dynamic cart interactions)
- **Django Templating Engine**

### Additional Packages
- **Pillow** (Image processing)
- **stripe** (Payment)

---

## Models Diagram

![Database Schema](screenshots/models-diagram.png)  

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
