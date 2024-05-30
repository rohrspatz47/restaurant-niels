# Restaurant Django Exercise

Download:

    $ git clone YOUR_FORKED_REPOSITORY_URL
    $ cd restaurant-django-exercise/

Create virtual environment:

    $ python -m venv .venv

Install dependencies:

    $ pip install -e .

Start development server:

    $ python manage.py runserver


## Week 1

Use the provided Django project template to implement a website for a restaurant.

The website should feature the following pages:

* a home page
* an about page
* a menu page
* a reservation page
* an order page (optional)

The home page and the about page are already provided.
The other pages are your task to build.

Create new Django apps for the menu, reservations and orders.

**Requirements:**

* Level 0 (minimum): All pages are available
* Level 1 (basic): The menu app is implemented
* Level 2 (intermediate): The reservations app is implemented
* Level 3 (advanced): The orders app is implemented


## Week 2

Use [Django REST Framework]() to create the following API endpoints:

    GET /api/menu 
    POST /api/reservations
    GET /api/reservations
    POST /api/orders
    GET /api/orders

**Requirements:**

* Level 0 (minimum): `GET /menu` is implemented
* Level 1 (basic): `GET /reservations` is implemented
* Level 2 (intermediate): `POST /reservations` is implemented
* Level 3 (advanced): `GET /orders` and `POST /orders` are implemented

Optional: Refactor the forms in such way that they access the API via JavaScript.# restaurant
