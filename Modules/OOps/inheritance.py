# class Animal:
#     def speak(self):
#         print("Animal Speaking")

# class Dog(Animal):
#     def bark(self):
#         print("Dog Barking")

# d = Dog()
# d.bark()
# d.speak()

# class Girl:
#     def purpose(self):
#         print("Girl Purpose")

# class Roshan(Girl):
#     def reject(self):
#         print("Roshan Reject")

# r = Roshan()
# r.reject()
# r.purpose()               


#Multiple Level Inheritance

# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
  
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  
 
# class DogChild(Dog):  
#     def eat(self):  
#         print("Eating bread...")  
# d = DogChild()  
# d.bark()  
# d.speak()  
# d.eat()
# d.eat()  


#Multiple Inheritance

# class Calculation1:  
#     def Summation(self,a,b):  
#         return a+b;  
# class Calculation2:  
#     def Multiplication(self,a,b):  
#         return a*b;  
# class Derived(Calculation1,Calculation2):  
#     def Divide(self,a,b):  
#         return a/b;  
# d = Derived()  
# print(d.Summation(10,20))  
# print(d.Multiplication(10,20))  
# print(d.Divide(10,20))


#The issubclass(sub,sup)

# class Calculation1:  
#     def Summation(self,a,b):  
#         return a+b;  
# class Calculation2:  
#     def Multiplication(self,a,b):  
#         return a*b;  
# class Derived(Calculation1,Calculation2):  
#     def Divide(self,a,b):  
#         return a/b;  
# d = Derived()  
# print(issubclass(Derived,Calculation2))  
# print(issubclass(Calculation1,Calculation2))  

#isinstance (obj, class) method

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(isinstance(d,Derived))