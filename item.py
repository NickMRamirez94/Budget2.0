class item(object):
    #class that will house information for one item

    def __init__(self, price, name, date):
        self.price = price
        self.name = name
        self.date = date

    def getPrice(self):
        return self.price
    
    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def setPrice(self, price):
        self.price = price

    def setName(self, name):
        self.name = name
    
    def setDate(self, date):
        self.date = date