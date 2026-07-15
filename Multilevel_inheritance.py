class Employee:
    def __init__(self) -> None:
        print("Employee Constructor")
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3

o = Employee()
print(o.a) # print the attribute 
#print(o.b) # Shows an error as there is no attribute in Employee Class 
o = manager()
print(o.a, o.b, o.c) # print the attribute of Employee Class