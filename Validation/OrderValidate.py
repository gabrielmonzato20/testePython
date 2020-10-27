from service.CustomerServer import CustomerService
from service.ProductService import ProductService


class OrderValidate:
    def __init__(self,data):
        self.data = data
        self.customerservice = CustomerService()
        self.productservice = ProductService()

    def ValidateCustomer(self):

        customer = self.customerservice.get(self.data['customer_id'])
        if customer is None:
            raise Exception("customer not find")

    def ValidateProduct(self):

        for product in self.data['products']:
            prod = self.productservice.get(product['id'])
            if prod is None:
                raise Exception("Product not find")
            if prod.stock < product['qtd']:
                raise Exception("not have stock enought")
            if product['qtd'] < 0 :
                raise Exception("the qtd must be greater then 0 ")

    def start(self):
        self.ValidateProduct()
        self.ValidateCustomer()
