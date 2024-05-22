class Person:
    def __init__ (self,name, age):
        self.name = name
        self.__age = age
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")
        
person = Person("Prasoon", 28)
person.__age = 30

person.display_details()