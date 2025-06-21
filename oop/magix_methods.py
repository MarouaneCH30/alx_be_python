class Student:
    def __init__(self, age, name, form):
        self.age = age
        self.name = name
        self.form = form
        
    #magic method 
    def __str__(self):
         return f" Name: {self.name} \n Age: {self.age} \n Form: {self.form}"
    
student1 = Student(15, 'Angie', 3)
print(student1)