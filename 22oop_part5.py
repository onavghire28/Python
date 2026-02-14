#Reference variable

class Person():

    def __init__(self):
        self.name = "Om"
        self.age = 24

p = Person()
q = p
print(id(p))
print(id(q)) 

q.name = "Ayush"
print(p.name)

#Object Mutabality

class Person:
    def __init__(self):
        self.name = "Om"

def change(obj):
    obj.name = "Ayush"

     
obj = Person()
print(obj.name)
change(obj)

print(obj.name)
