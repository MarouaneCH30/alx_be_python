#class methods = allow operations related to the class itself
#Takes (cls) as the first parameter, which represent the class itself
#These are methods that are bound to the class itself rather than instances of the class(objects)
#They are used to define methods that operate on class-level data or perform operations related to the class


#Example from alx
class Animal:
    count = 0
    def __init__(self, name):
        self.name = name
        Animal.count += 1
        
    @classmethod
    def display_count(cls):
        print(f"Total number of created Animal instances: {cls.count}")
    

animal1 = Animal('Cat')
animal2 = Animal('Dog')
animal3 = Animal('Cow')

Animal.display_count()


#Example from Bro Code - Youtube

class Student:
    count = 0
    total_gpa = 0
    average_gpa =0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        Student.average_gpa = Student.total_gpa / Student.count
    
    def get_student_info(self):
        print(f"Student Name: {self.name} GPA: {self.gpa}")
    
    #this classmethod keeps count    
    @classmethod
    def student_count(cls):
        print(f"Total number of students: {cls.count}")
        
    #this classmethod calculates total number of gpa
    @classmethod
    def calculate_gpa(cls):
        print(f'Total gpa = {cls.total_gpa}')
    
    @classmethod 
    def average_class_gpa(cls):
       if cls.count == 0:
           return 0
       else:
            print(f"The class average gpa : {cls.average_gpa:.2f}")



student1 = Student(name= 'Mercy', gpa= 7.9)
student2 = Student(name= 'Achieng', gpa= 8.9)
student3 = Student(name= 'Cate', gpa= 7.2)
student4 = Student(name= 'Melvine', gpa= 9.9)

Student.student_count()
Student.calculate_gpa()
Student.average_class_gpa()

        