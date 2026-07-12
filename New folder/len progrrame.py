name = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(len(name))
user_name = input("Enter your name: "). title()

if user_name in name:
    print("Name found in the list.")
else:
    print("Name not found in the list.")