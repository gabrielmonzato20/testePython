from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from .Base  import db

class Customer(db.Model):

    __tablename__ = 'customers'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(50))
    adress = Column(db.String(20))
    cpf = Column(db.String(15))
    orders = db.relationship('Order', backref=db.backref("customers", lazy="joined"), lazy="select"
    )


    def toJson(self):
        return {
            "id": self.id,
            "name":self.name,
            "adress":self.adress,
            "cpf": self.cpf

        }
