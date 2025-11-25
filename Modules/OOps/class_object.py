class Person:
    def __init__  (self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello,my name is" + self.name)    

p1 = Person("Icon",21)
p1.greet()


#Class and Instance Variables

class Person:
    count = 0

    def __init__ (self,name,age):
      self.name = name
      self.age = age
      Person.count += 1

p1 = Person("Icon",21)
p2 = Person("Chidku",22)
#print(Person.count)  

print(p1.name)
print(p2.age)   



        


