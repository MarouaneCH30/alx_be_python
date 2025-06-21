#@property = Decorator used to define a method as a property, it can be accessed like an attribute
#Benefits: Add additional logic when read, write or delete attribute
# Gives you getter, setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
     
    @property   
    def width(self):     #getter property
        return f"{self._width:.2f}cm"   
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
            return new_width
        else:
            print("Width must be greater than zero")
    
    @property
    def height(self):
        return f"{self._height:.2f}cm"
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
            return new_height
        else:
            print("Height must be greater than zero")
    
    
    


rectangle = Rectangle(width= 10, height= 20)

rectangle.width = int(input("Enter new Width: "))
rectangle.height = int(input("Enter new Height: "))

print(rectangle.width)
print(rectangle.height)