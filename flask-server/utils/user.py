from server import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_nubmer = db.Column(db.Integer, nullable=True)
    first_name = db.Column(db.String(10), nullable=True)
    last_name = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return f"User(user_id = {self.user_id}, username = {self.username}, email = {self.email})"

db.create_all()