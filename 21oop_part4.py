#object access

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        if self.age >= 18:
            print("Able to vote")

        else:
            print("Not able to vote")

obj = Person("Om",22)

print(obj.name)
print(obj.age)
obj.greet()
        