from flask import Flask, request
from flask_restful import Api, Resource, marshal_with, reqparse, abort, fields
import os
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from __init__ import *
import pymysql


app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///database.db"
app.config["SQLALCHEMY_ECHO"] = True
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
            return {"Success": False, "Status Code": 400}, 400

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

            user = User(username=args["username"], password=args["password"], email=args["email"], phone_nubmer=args["phone number"],
            first_name=args["first name"], last_name=args["last name"])
            db.session.add(user)
            db.session.commit()
            return {"Success": True, "Status Code": 201}, 201
        
        return {"Success": False, "Status Code": 400}, 400


class Usernames(Resource):
    usernames_post_args = reqparse.RequestParser()
    usernames_post_args.add_argument("username", type=str, help="username is required to requests name", required=True)

    def post(self):
        args = self.usernames_post_args.parse_args()

        user = User.query.filter_by(username=args["username"]).first()
        if user is None:
            return {"Status Code": 200, "found": False, "message": "Username is not exists"}, 200

        return {"Status Code": 200, "found": True, "message": "Username is already exists"}, 200


class CreateShop(Resource):
    shop_put_args = reqparse.RequestParser()
    shop_args = ["username", "shop_name"]
    shop_args_help = ["Username that the shop belongs to", "shop name ._."]
    args_required = [True, True]
    for i in range(2):
        shop_put_args.add_argument(shop_args[i], type=str, help=shop_args_help[i], required=args_required[i])

    def put(self):
        args = self.shop_put_args.parse_args()
        user = User.query.filter_by(username=args["username"]).first()

        if user is None:
            return {"Success": False, "message": f"There is no user named {args['username']}", "Status Code": 400}, 400

        shop = Shop(author_id=user.user_id, shop_name=args["shop_name"])
        db.session.add(shop)
        db.session.commit()

        return {"Success": True, "Status Code": 200}, 200

class CreateItem(Resource):
    item_put_args = reqparse.RequestParser()
    item_args = ["shop_name", "categories", "item_name"]
    item_args_help = ["Shop name that the item belongs to", "item categories", "item name is required"]
    args_required = [True, True, True]
    for i in range(3):
        item_put_args.add_argument(item_args[i], help=item_args_help[i], type=str, required=args_required[i])

    def put(self):
        args = self.item_put_args.parse_args()
        shop = Shop.query.filter_by(shop_name=args["shop_name"]).first()

        if shop is None:
            return {"Success": False, "message": f"There is no shop name named {args['shop_name']}", 'Status Code': 400}, 400

        item = Item(shop_id=shop.shop_id, item_name=args["item_name"], categories=args["categories"])
        db.session.add(item)
        db.session.commit()

        return {"Success": True, "message": f"create item in shop {args['shop_name']}", "Status Code": 200}, 200

api.add_resource(Login, "/login")
api.add_resource(SignUp, "/signup")
api.add_resource(Usernames, "/usernames")
api.add_resource(CreateShop, "/createShop")
api.add_resource(CreateItem, "/createItem")


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0') # (debug=True) Only run in development env **only**
