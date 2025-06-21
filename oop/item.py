import csv

class Item:
    all = []
    def __init__(self, name: str, price: float,  quantity = 0):
        
        assert quantity >=0, 'Quantity cannot be less than Zero'
        assert price >=0, 'Price cannot be less than Zero'
        self.__name = name
        self.__price = price
        self.quantity = quantity
       
        Item.all.append(self) 
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        print('You are trying to set new name')
        self.__name = value
        
    @classmethod
    def instantiate_from_csv(cls):
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity'))
                
            )
    def apply_increment(self, increment):
        self.__price = self.__price + self.__price * increment
        
       