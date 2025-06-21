# a child inherits from multiple parent classes

class Flyer:
  def fly(self):
      print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

#this below child class inherites from both the Flyer and Swimmer classes

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()