from __init__ import db
from uuid import uuid4

def gen_uuid():
    return uuid4().hex

class Shop(db.Model):
    author_id = db.Column(db.String(32), primary_key=True, unique=True, nullable=False)
    shop_id = db.Column(db.String(15), unique=True, nullable=False, default=gen_uuid)
    items = db.relationship('Item', backref='shop', lazy=True)

    def __repr__(self):
        return f"Shop(Author_id: {self.author_id}, shop_id: {self.shop_id}, item: {self.items})"

class Item(db.Model):
    item_id = db.Column(db.String(15), primary_key=True, unique=True, default=gen_uuid)
    shop_id = db.Column(db.String(15), db.ForeignKey("shop.id"), nullable=False)
    item_name = db.Column(db.String(20), unique=False, nullable=False)
    categories = db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return f"Item(Shop Id: {self.shop_id}, Item name: {self.item_name})"

db.create_all()