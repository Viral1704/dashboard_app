from .extensions import db

from datetime import datetime

from sqlalchemy.sql import func

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer) 
    monthly_goal = db.Column(db.Integer)

    def revenue_this_month(self):
        first_of_month = datetime.today().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )

        return db.session.query(func.sum(Order.quantity * self.price)).filter(Order.product_id == self.id, Order.date > first_of_month).scalar() or 0


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
