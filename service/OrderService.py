from model.Base import db
from model.Order import Order
from service.ProductService import ProductService
from service.CustomerServer import CustomerService
from model.Order import association_table
class OrderService:
    def __init__(self):
        self.customer = CustomerService()
        self.product = ProductService()

    def save(self,data):

        try:
            order = Order()
            order.customer_id= data['customer_id']
            db.session.add(order)
            db.session.commit()
            for product in list(data['products']):
                insert = association_table.insert().values(order_id =order.id,
                                                           product_id=product["id"],
                                                           qtd=product["qtd"])
                db.session.execute(insert)
            db.session.commit()
        except Exception as e:
            raise Exception("we cant save the row",e)
        return 'Order Save sucessful' ,200

    def update(self,data,id):

        order = Order.query.filter_by(id=id).first()
        try:
            if order is not None:

                order.customer_id = self.customer.get(data['customer_id'])
                db.session.add(order)
                db.session.commit()
                delete =association_table.delete().where(order_id=order.id)
                db.session.execute(delete)
                db.session.commit()
                for product in data['products']:
                    insert = association_table.insert().values(order_id=order.id, product_id=product.id,
                                                               qtd=product.qtd)
                    db.session.execute(insert)
                db.session.commit()
                menssage = "Update the row " + str(order.id)
            else:
                menssage = "Id not exists"
        except :
            raise Exception("Sorry, we can t save this row!")
        return menssage

    def delete(self, id):

        order = Order.query.filter_by(id=id).first()
        try:
            if order is not None:
                delete = association_table.delete().where(order_id=order.id)
                db.session.execute(delete)
                db.session.commit()
                db.session.delete(order)
                db.session.commit()
                menssage = "Delete the row " + str(order.id)
            else:
                menssage = "Id not exists"
        except Exception as e:
            raise Exception("Sorry, we can t delete this row!" , e)
        return menssage

    def read(self, id):

        order = Order.query.filter_by(id=id).first()
        try:
            if order is not None:

                return order.toJson()
            else:
                menssage = "Id not exists"
        except:
            raise Exception("Sorry, we can t find this row!")
        return menssage

    def readAll(self):

        try:
            order = Order.query.all()
            orders = []
            for x in order:

                orders.append(x.toJson())
        except Exception as e:
            raise Exception("error==>",e)
        return str(orders)