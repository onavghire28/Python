#Super keyword

class person:

    def __init__(self,name):
        self.name = name

class user(person):

    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno = rollno 

obj = user("Om",12)
print(obj.name)


#Example no 2
class p1:

    def greet(self):
        print("Welcome p1")

class p2(p1):

    def greet(self):
        super().greet()
        print("Welcome p2")

obj = p2()
obj.greet()