import click

from flask.cli import with_appcontext

from .extensions import db
from .models import Customer, Product, Order


@click.command('create_tables')
@with_appcontext
def create_tables():
    db.create_all()


@click.command('create_products')
@with_appcontext
def create_products():
    product1 = Product(name = 'First Product', price = 10, monthly_goal = 1000)
    product2 = Product(name = 'Second Product', price = 25, monthly_goal = 4000)
    product3 = Product(name = 'Third Product', price = 90, monthly_goal = 3000)

    db.session.add_all([product1, product2, product3])
    db.session.commit()
    