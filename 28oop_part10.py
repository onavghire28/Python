#method overriding

class animal:
    def color(self):
        return "color is Brown"
    
    def sound(self):
        return "Animal is barking"
    
class Dog(animal):

    def sound(self):
        return "dog is barking" 

d = Dog()
a = animal()

print(a.sound())
print(d.sound()) 
print(d.color())      