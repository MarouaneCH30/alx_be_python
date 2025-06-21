#class is the blueprint of creating objects
#Objects are instance/ occurence of class
class Sport:
    rules = []
    is_indoor = False
    #methods shows the action/ behaviour of the objects
    def play():
        print()
class Person:
    name =""
    age = 20
    family =""
class Farm:
    pass

football = Sport() #object
basketball = Sport()

print(football is basketball)