from flask import request

import service.ProductService
from flask_classful import FlaskView, route

from Validation.ProductValidate import ProductValidate


class ProductController(FlaskView):


    def __init__(self):
        self.serve = service.ProductService.ProductService()

    @route("/save",methods=['POST'])
    def save(self):

        data = request.get_json()
        ProductValidate(data).start()
        return self.serve.save(data)

    @route("/update/<int:id>",methods=['POST'])
    def update(self,id):
        data = request.get_json()
        ProductValidate(data).start()
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