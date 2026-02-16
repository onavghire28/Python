#Aggregation in oop

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Department:
    def __init__(self,dep_name,emp):
        self.dep_name = dep_name
        self.emp = emp

    def print_info(self):
        print("Name: ",self.emp.name)
        print("Salary:",self.emp.salary)
        print("dep_name:",self.dep_name)  
        
obj = Employee("Om",25000)
L = Department("IT",obj)

L.print_info()