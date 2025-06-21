def division():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            
            if num2 == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('You can not devide a number by zero!')
        
        except Exception:
            print("Enter a valid number!")
        
        else:
            print(f"The quotient from {num1} / {num2} is",num1/num2)
            
        
            
        finally:
            print("Bye!")
        break
            
division()