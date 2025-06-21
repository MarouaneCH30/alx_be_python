class Human:
    def eat(self):
        pass
class Male:
    def flirt(self):
        pass
class Boy(Human,Male):
    pass

boy1 = Boy()
boy1.eat()