class Human:
    
    def __init__(self, name,age):
        
        self.name = name
        self. age =age
        
         
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
        
class Male(Human):
    
    def __init__(self, career, education, name,age):
        self.career = career
        self.education = education
        super().__init__(name,age)
    def work(self):
        super().work()
        print("I can code using python")
        
    def display_info(self):
        
        print(f"My name is {self.name}\nCareer: {self.career} \nEducation: {self.education} \n Age: {self.age}")
        




male1 = Male('Engineer','Masters', 'Gucha',24)

male1.display_info()