#Encapsulation

class Person:

    def __init__(self):
        self.name = "Om"  #Public
        self.__age = 18   #Private

p = Person()
print(p.name)
#print(p.__age)  #-> we can not access this attribute

class Info:

    def __init__(self):
        self.name = "Om"
        self.__age = 18

    def getter(self):
        print(self.__age) 
    
    def setter(self,new_age):
        self.__age = new_age
        print(new_age)

obj = Info()
obj.getter()
obj.setter(45)