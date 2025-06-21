class ValueTooHighError(Exception):
    def __init__(self,value, message="Value exceeds the allowed 100 limit."):
        self.value = value
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.value} {self.message} "
    
def check_value():
        try:
            value =int(input("Enter a number: "))
            if value > 100:
                raise ValueTooHighError(value)
        except ValueTooHighError as e:
            print(e)
        
        except Exception:
            print("Invalid input")
        
        else:
            print(f"The number {value} is in the desired range, proceed on")
        
        finally:
            print("Bye!")
            
check_value()
    
 