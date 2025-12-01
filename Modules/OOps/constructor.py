#creating constructor in pythyon

class Employee:
    def __init__ (self,name,id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))

emp1 = Employee("Roshan",101) 
emp2 = Employee("Vedant",420) 

emp1.display()
emp2.display()    


#counting number of objects in classs
class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count) 