from __init__ import db

class Shop(db.Model):
    author_id = db.Column(db.String(15), primary_key=True, unique=True, nullable=False)
    shop_id = db.Column(db.String(15), unique=True, nullable=False)
    item = db.relationship('Item', backref='Shop', lazy=True)

    def __repr__(self):
        return f"Shop(Author_id: {self.author_id}, shop_id: {self.shop_id}, item: {self.item})"

class Item(db.Model):
    shop_id = db.Column(db.String(15), primary_key=True, unique=True, nullable=False)
    item_name = db.Column(db.String(20), unique=False, nullable=False)

db.create_all()