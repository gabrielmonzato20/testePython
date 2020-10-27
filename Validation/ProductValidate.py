class ProductValidate:

    def __init__(self,data):
        self.data = data

    def stockvalid(self):

        if self.data["stock"] > 0:
            return True
        raise Exception("stock most be greater then 0")

    def valuevalid(self):

        if self.data["value"] >= 0:
            return True
        raise Exception("value most be greater then 0")

    def start(self):

        self.stockvalid()
        self.valuevalid()