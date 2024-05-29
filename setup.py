from setuptools import setup, find_packages

setup(
    name='restaurant-django-exercise',
    version='0.0.1',
    packages=find_packages(),
    description='Restaurant Django Exercise',
    author='Niels Hoppe',
    author_email='mail@nielshoppe.de',
    install_requires=[
        'Django',
        'django-filter',
        'djangorestframework',
        'markdown',
        ]
    )