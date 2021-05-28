class Student:
    school="Akirachix"
#to create a class use a class keyword
#start the class name with a capital letter.if it has more than one letter capitalize each word
#do not include spaces
#many modules in a directory form a package
#when you save your code oin a .py file its called a module
#to import a class from any module use . notation eg-from module import class name (import convection) standard libraries,built in modules.
#object creation from class instance creation
#def__init__(Self,name,age) creating a class contructor self is refers to instance of class
    def __init__(self,name,age,unit):
       self.name=name#assignning variables to class instance
       self.age=age
       self.unit=unit
       
    def speak(self):
        return f"Hello my name is {self.name} and I am {self.age} years old"
    def learn(self):
        return f"I am studying {self.unit} in{self.school}"

        #create class Car : give it 4 attributes(),behaviour()3,
        #create class Dog attributes(3) ,method(1)
        #bank.py class Account(3)method(2)
        
