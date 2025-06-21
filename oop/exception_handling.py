while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

def division():
    #Handling exceptions
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num1 / num2
        
    except ZeroDivisionError:
        print("You can not divide by zero, enter another number")
    
    except ValueError:
        print("Enter a valid input - Integers only")
    
    except Exception:
        print('Something Went wrong!')
    else:
        print(num1/num2)
    
    finally:
        print("Bye!")
        

division()


#Creating Custom Exceptions

class OutofStockError(Exception):
    def __init__(self, item_name):
        self.item_name = item_name
    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."
    
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  
    "grapes": 3
}


def check_for_product():
    product = input("Enter the product you want to purchase: ").lower()
    
    try:
        if  product in product_inventory == 0:
            print("The product is available for purchase")
        else:
            raise OutofStockError
    except OutofStockError:
        
     error = OutofStockError()
     error.__str__
    else:
        print("The product is available for purchase")
    finally:
        print("Thank you for shopping with")
        

check_for_product()