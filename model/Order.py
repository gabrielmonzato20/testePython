from sqlalchemy.orm import relationship

from service.CustomerServer import CustomerService
from .Base import db
from .Customer import Customer
association_table = db.Table('ProductOrder',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('qtd',db.Integer),
)

class Order(db.Model):

    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey('customers.id'))
    products = db.relationship("Product",secondary=association_table,
                               backref="orders",
                               lazy='select')

    def toJson(self):
        return {
            "id": self.id,
            "customer": self.customerParser(),
         "products": list(map(lambda x: x.toJson(),self.products))
        }

    def customerParser(self):

        try:
            customer = CustomerService()
            c = customer.get(self.customer_id)
            return c.toJson()
        except Exception as e:
            raise Exception("error ==>", e)