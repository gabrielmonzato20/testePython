from controller.OrderController import OrderController
from env.Config import SQLALCHEMY_DATABASE_URI
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller.CustomerController import CustomerController
from controller.ProductController import ProductController
from sqlalchemy_utils import database_exists, create_database
from model.Base import config_db ,db

class init():

    def __init__(self):
        self.app = Flask(__name__,instance_relative_config=True)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
        config_db(self.app)
        self.customerservice = CustomerController()
        self.productservice = ProductController()
        self.orderservice = OrderController()


if __name__ == "__main__":

    app = init()
    engine = db.create_engine(SQLALCHEMY_DATABASE_URI, {})
    if  not database_exists(engine.url):
        create_database(engine.url)
    with app.app.app_context():
        db.create_all()
    app.customerservice.register(app.app, route_base="/customer")
    app.productservice.register(app.app,route_base='/product')
    app.orderservice.register(app.app,route_base="/order")
    app.app.run(debug=True, host='0.0.0.0')



