#Inheritance

class Parent:

    def __init__(self):
        self.name = "Om"
        self.salary = 25000

    def login(self):
        print("welcome")   

class Child(Parent):

    def enroll(self):
        print("Thank you")

p = Parent()
c = Child()
print(c.name)  #parent attribute
print(c.salary)  #parent attribute

c.login()  #parent method
c.enroll()