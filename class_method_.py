class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class Attribute of a is  {cls.a}")


e = Employee()
e.a = 45

e.show()  # Output: Employee Class Method: a is 1
