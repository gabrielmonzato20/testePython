from flask import request
from flask_classful import FlaskView, route

import service.OrderService
from Validation.OrderValidate import OrderValidate


class OrderController(FlaskView):
    def __init__(self):
        self.serve = service.OrderService.OrderService()

    @route("/save",methods=['POST'])
    def save(self):

        data = request.get_json()
        OrderValidate(data).start()
        return self.serve.save(data)

    @route("/update/<int:id>",methods=['POST'])
    def update(self,id):
        data = request.get_json()
        OrderValidate(data).start()
        return self.serve.update(data,id)

    @route("/delete/<int:id>",methods=['DELETE'])
    def delete(self,id):

        return self.serve.delete(id)

    @route("/<int:id>",methods=['GET'])
    def read(self,id):

        return self.serve.read(id)

    @route("/",methods=['GET'])
    def readAll(self):

        return self.serve.readAll()