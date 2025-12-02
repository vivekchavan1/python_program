from abc import ABC,abstractmethod

class vehicle(ABC):
   def start(self):
      pass
   
   def stop(self):
      pass
   
class Car(vehicle):
   def start(self):
      print("Car is starting with a key ignition.")

   def stop(self):
      print("Car is stopping using the brake.")

my_car = Car()  
my_car.start()  
my_car.stop() 



from abc import ABC,abstractmethod
class Animal(ABC):
   
   def make_sound(self):
      pass
   
class Dog(Animal):
   def make_sound(self):
      return "Bark!"
   
class Cat(Animal):
   def make_sound(self):
      return "Meow!"


dog = Dog()  
cat = Cat()  
  
print(dog.make_sound())    
print(cat.make_sound())          

   
      

   