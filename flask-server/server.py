from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from utils.user import *

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('host')}/vshop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db.create_all()

class Login(Resource):
    login_get_args = reqparse.RequestParser()
    login_args = ["username", "password"]
    login_help = ["user username is required to login", "password is required to login"]
    for i in range(2):
        login_get_args.add_argument(login_args[i], type=str, help=login_help[i], required=True)

    def post(self):
        args = self.login_get_args.parse_args()

        user = User.query.filter_by(username=args["username"], password=args["password"]).first()
        print(user)

        return {"UserExists": True}

api.add_resource(Login, "/login")


if __name__ == '__main__':
    app.run(debug=True) # (debug=True) Only run in development env **only**