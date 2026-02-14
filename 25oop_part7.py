#object collection

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Om",18)
p2 = Person("Ayush",21)
p3 = Person("Pratham",24)

l = [p1,p2,p3]

for i in l:
    print(i.name,i.age)