# Furniture Shop Ecommerce (Django)

![Project Banner Image](path/to/banner-image.png)  
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

While still a work in progress, it demonstrates key ecommerce concepts and a clean, responsive design.

---

## Features

- Product listing with category filters and search  
- User account profile editing  
- Dynamic cart updates (using htmx)  
- Image thumbnail generation for consistent product display  
- Responsive design with Tailwind CSS  
- Admin dashboard for product and category management  

---

## Tech Stack

- Python 3.x  
- Django 4.x  
- Pillow (for image processing)  
- Tailwind CSS (via CDN or installed)  
- HTMX (for dynamic cart updates)  
- SQLite (default, can be replaced with PostgreSQL or MySQL)  

---

## Models Diagram

Below is a diagram showing the core database models and their relationships, generated using pydot:

![Models Diagram](path/to/models-diagram.png)  
*Replace this with your generated PNG from your pydot graph.*

---

## Installation

1. Clone the repo:  
   ```bash
   git clone https://github.com/yourusername/furniture-shop.git
   cd furniture-shop
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser for admin access:

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.

Usage
Use the search and category filters on the shop page to browse products.

Click a product to view details and add to your cart dynamically.

Edit your account profile in the "My Account" section.

Admin users can add/edit products and categories via /admin.

Screenshots
<!-- Add screenshots here -->



Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.