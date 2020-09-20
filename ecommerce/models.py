from ecommerce import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.Integer,unique=True,nullable=False)
    password = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return f"User('{self.id }',{self.first_name}', '{self.last_name}', '{self.email}','{self.created_at}','{self.admin}')"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(60),nullable=False,unique=True)
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.id}','{self.name}','{self.product_category}')"

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20),nullable=False)
    description = db.Column(db.Text, nullable=False)
    price =db.Column(db.Float ,nullable=False)
    picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    quantity = db.Column(db.Integer , nullable=False ,default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

   
    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.image_file}','{self.price}','{self.quantity}')"



