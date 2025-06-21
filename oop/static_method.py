#Static methods are independent of class instances and the class itself
#They behave like regular functions but are defined inside a class for organization purposes
#They are defined using the @staticmethod decorator and don’t require the self or cls parameter.

#Example from alx

class BasicArithmetics:
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            print("You can not divide by zero!")


print(f" Sum : {BasicArithmetics.add(10, 5)}")
print(f"Difference: {BasicArithmetics.subtract(10, 5)}")
print(f"Product: {BasicArithmetics.multiply(3, 6)}")
print(f"Quotient: {BasicArithmetics.division(12, 3)}")



#Example from Bro code = youtube

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_employee_info(self):
        return f"Employee Name: {self.name} Employee Position: {self.position}"
    
    
    @staticmethod
    def is_valid_position(position):
        
        valid_positions = ['manager', 'cook', 'janitor', 'cashier']
        
        if position in valid_positions:
            print(f"{position} is a valid position here")
        else:
            print("This is not a valid position here!")
    

Employee.is_valid_position(position= 'manager')
        
        
    