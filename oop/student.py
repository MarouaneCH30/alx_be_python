
class Student:
    
    def __init__(student, name, admission_number, age, course):
        student.name = name
        student.admsission_number = admission_number
        student.age = age
        student.course = course
        
    def display_student_details(student):
        
        print(f" Here are the student's details: \n Name: {student.name}\n Admission Number: {student.admsission_number}\n Age: {student.age} years old \n Course: {student.course}")
        
student1 = Student('Gucha',15722, 24, 'Electrical Engineering')

student1.display_student_details()
    