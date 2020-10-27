from sqlalchemy import Column, Integer, String, Float

from .Base import db

# model definiton of product
class Product(db.Model):

    __tablename__ = 'products'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(50))
    value = Column(db.Float)
    description =  Column(db.String(50))
    stock = Column(db.Integer)

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "stock": self.stock,
            "value": self.value
        }