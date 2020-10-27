from model.Product import Product
from model.Base import db

class ProductService():

    def save(self,js):

        try:
            product = Product()
            product.name = js["name"]
            product.description = js["description"]
            product.stock = js["stock"]
            product.value = js['value']
            db.session.add(product)
            db.session.commit()
        except Exception as e:
            raise Exception("Sorry, we can t save this row!",e)
        return product.toJson()


    def update(self,js,id):

        product = Product.query.filter_by(id=id).first()
        try:
            if product is not None:

                product.name = js["name"]
                product.description = js["description"]
                product.stock = js["stock"]
                product.value = js['value']
                db.session.add(product)
                db.session.commit()
                menssage = "Update the row " + str(product.id)
            else:
                menssage = "Id not exists"
        except :
            raise Exception("Sorry, we can t save this row!")
        return menssage

    def delete(self, id):

        product = Product.query.filter_by(id=id).first()
        try:
            if product is not None:

                db.session.delete(product)
                db.session.commit()
                menssage = "Delete the row " + str(product.id)
            else:
                menssage = "Id not exists"
        except Exception as e:
            raise Exception("Sorry, we can t delete this row!" , e)
        return menssage

    def read(self, id):

        product = Product.query.filter_by(id=id).first()
        try:
            if product is not None:
                return product.toJson()
            else:
                menssage = "Id not exists"
        except:
            raise Exception("Sorry, we can t find this row!")
        return menssage

    def get(self,id):

        product = Product.query.filter_by(id=id).first()
        try:
            if product is not None:
                return product
            else:
                menssage = "Id not exists"
        except:
            raise Exception("Sorry, we can t find this row!")
        return menssage

    def readAll(self):

        product = Product.query.all()
        products = [x.toJson() for x in product]
        return str(products)



