from server import db

class User(db.Model):
    user_id = db.Column(db.String(15), primary_key=True, unique=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_nubmer = db.Column(db.Integer, nullable=True)
    first_name = db.Column(db.String(10), nullable=True)
    last_name = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        user_dict = {'user_id': self.user_id, 'username': self.username, 'password': self.password, 'email': self.email, 
        'phone number': self.phone_nubmer, 'first_name': self.first_name, 'last_name': self.last_name}
        return f"{user_dict}"

db.create_all()