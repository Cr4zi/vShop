from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from utils.user import *
import random

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('host')}/vshop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db.create_all()

class Login(Resource):
    login_post_args = reqparse.RequestParser()
    login_args = ["username", "password"]
    login_help = ["user username is required to login", "password is required to login"]
    for i in range(2):
        login_post_args.add_argument(login_args[i], type=str, help=login_help[i], required=True)

    def post(self):
        args = self.login_post_args.parse_args()

        user = User.query.filter_by(username=args["username"], password=args["password"]).first()
        print(user)

        return {"UserExists": True}

class SignUp(Resource):
    signup_put_args = reqparse.RequestParser()
    signup_args = ["username", "password", "email", "phone number", "first name", "last name"]
    signup_help = ["user username is required to login", "password is required to login", "email is required to login", 
    "phone number is not required to login", "first name is not required to login", "last name is not required to login"]
    signup_required = [True, True, True, False, False, False]
    for i in range(6):
        signup_put_args.add_argument(signup_args[i], type=str, help=signup_help[i], required=signup_required[i])

    def put(self):
        args = self.signup_put_args.parse_args()

        user = User.query.filter_by(username=args["username"], password=args["password"]).first()
        if user is None:

            # def generate_id():
            #     usr_id = random.randint(100000000000, 1000000000000)
            #     user = User.query.filter_by(user_id=generate_id())
            #     if user is not None:
            #         return generate_id()
            #     return usr_id

            id = random.randint(1000000000, 4294967295)

            user = User(user_id=str(id), username=args["username"], password=args["password"], email=args["password"], phone_nubmer=args["phone number"],
            first_name=args["first name"], last_name=args["last name"])
            db.session.add(user)
            db.session.commit()
            return {"Success": True, "Status Code": 201}, 201
        
        return {"Success": False, "Status Code": 400}


api.add_resource(Login, "/login")
api.add_resource(SignUp, "/signup")


if __name__ == '__main__':
    app.run(debug=True) # (debug=True) Only run in development env **only**