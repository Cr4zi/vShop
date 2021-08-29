from flask import Flask, request
from flask_restful import Api, Resource, marshal_with, reqparse, abort, fields
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from __init__ import *
import random
import pymysql

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('host')}/vshop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db.create_all()

login_fields = {
    "user_id": fields.String,
    "username": fields.String,
    "password": fields.String,
    "email": fields.String,
    "phone number": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
}

class Login(Resource):
    login_post_args = reqparse.RequestParser()
    login_args = ["username", "password"]
    login_help = ["user username is required to login", "password is required to login"]
    for i in range(2):
        login_post_args.add_argument(login_args[i], type=str, help=login_help[i], required=True)

    @marshal_with(login_fields)
    def post(self):
        args = self.login_post_args.parse_args()

        user = User.query.filter_by(username=args["username"], password=args["password"]).first()
        if user is None:
            return {"Success": False, "Status Code": 400}

        # return {"Success": True, "user": user,"Status Code": 201}, 201
        return user, 200

class SignUp(Resource):
    signup_put_args = reqparse.RequestParser()
    signup_args = ["username", "password", "email", "phone number", "first name", "last name"]
    signup_help = ["user username is required to signup", "password is required to signup", "email is required to signup", 
    "phone number is not required to signup", "first name is not required to signup", "last name is not required to signup"]
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

            user = User(user_id=str(id), username=args["username"], password=args["password"], email=args["email"], phone_nubmer=args["phone number"],
            first_name=args["first name"], last_name=args["last name"])
            db.session.add(user)
            db.session.commit()
            return {"Success": True, "Status Code": 201}, 201
        
        return {"Success": False, "Status Code": 400}


class Usernames(Resource):
    usernames_post_args = reqparse.RequestParser()
    usernames_post_args.add_argument("username", type=str, help="username is required to signup", required=True)

    def post(self):
        args = self.signup_put_args.parse_args()

        user = User.query.filter_by(username=args["username"]).first()
        if user is None:
            return {"Success": True, "Status Code": 201}, 201

        return {"Success": False, "Reason": "username already exists","Status Code": 400}



api.add_resource(Login, "/login")
api.add_resource(SignUp, "/signup")
api.add_resource(Usernames, "/usernames")


if __name__ == '__main__':
    app.run(debug=True) # (debug=True) Only run in development env **only**