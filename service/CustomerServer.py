from model.Customer import Customer
from model.Base import db

class CustomerService():

    def save(self,js):

        try:
            customer = Customer()
            customer.name = js["name"]
            customer.cpf = js["cpf"]
            customer.adress = js["adress"]
            db.session.add(customer)
            db.session.commit()
        except Exception as e:
            raise Exception("Sorry, we can t save this row!",e)
        return customer.toJson()


    def update(self,js,id):

        customer = Customer.query.filter_by(id=id).first()
        try:
            if customer is not None:
                customer.name = js["name"]
                customer.cpf = js["cpf"]
                customer.adress = js["adress"]
                db.session.add(customer)
                db.session.commit()
                menssage = "Update the row " + str(customer.id)
            else:
                menssage = "Id not exists"
        except :
            raise Exception("Sorry, we can t save this row!")
        return menssage

    def delete(self, id):

        customer = Customer.query.filter_by(id=id).first()
        try:
            if customer is not None:

                db.session.delete(customer)
                db.session.commit()
                menssage = "Delete the row " + str(customer.id)
            else:
                menssage = "Id not exists"
        except Exception as e:
            raise Exception("Sorry, we can t delete this row!" , e)
        return menssage
    def get(self,id):

        customer = Customer.query.filter_by(id=id).first()
        try:
            if customer is not None:
                return customer
            else:
                menssage = "Id not exists"
        except:
            raise Exception("Sorry, we can t find this row!")
        return menssage

    def read(self, id):

        customer = Customer.query.filter_by(id=id).first()
        try:
            if customer is not None:
                return customer.toJson()
            else:
                menssage = "Id not exists"
        except:
            raise Exception("Sorry, we can t find this row!")
        return menssage

    def readAll(self):

        customer = Customer.query.all()
        customers = [x.toJson() for x in customer]
        return str(customers)