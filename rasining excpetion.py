a = int(input("enter a number:"))
b = int(input("enter second number:"))

if (b == -0):
    raise ZeroDivisionError("hey our programe is not meant to divide number by zero")

else:

    print(f" the divison a/b is {a/b}")
