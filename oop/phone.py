from item import Item         
class Phone(Item):
   
    def __init__(self, name, price, brocken_phones =0, quantity=0):
        super().__init__(name, price, quantity)
        
        self.brocken_phones = brocken_phones
        
        
        
print(Item.all)
 