#File Handling
# text, Binary
#modes: 'r', 'w', 'a', 'rb', 'wb'

#Create a file
# f = open("sample.txt", "w")
# f.write("Hello students!\nWelcome to File Handling.")
# f.close()

#Read a file
# f = open("sample.txt", 'r')
# data = f.read()
# print(data)
# f.close()
# f = open("sample.txt", 'r')
# print(f.read(10))
# print(f.readlines())

# Appena Mode
# f = open("sample.txt", 'a')
# f.write("nThis is a new line added by python")
# f.close()

# use with (Best Practice)
# with open("sample.txt", 'r') as file:
#     print(file.read())
# with open("Figure_2.png", "rb") as f:
# content = f.read()
# print(len(content), "bytes read")

# Create a file student.txt with 5 names
# read the file and print each name on a separate line
# append a new name and read

#Error Handling
#Syntax error
# if True
# print()

# try:
#     num = int(input("Enter a number: "))
#     print(10/num)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Invalid Input! Please enter a number!")

# try:
#     f = open('text.txt', 'r')
#     print(f.read())
# except FileNotFoundError:
#     print("File Not found!")
# finally:
    # print("Execution completed!")

# age = int(input("Enter your age: "))
# if age < 18:
    # raise ValueError("You must be at least 18 years old")

#Function
# def greet():
#     print("Hello Students")
# greet()

# def add(a, b):
    # c = a + b
    # return c
# ans = add(2, 3)
# ans2 = add(10, ans)
# print(ans2)

# def greet(name):
#     print("Hello", name)
# greet("Varshita")

# def greet(name="Guest"):
#     print("Hello", name)
# greet()

# def intro(name, age):
    # print(f"My name is {name} and I'm {age} years old.")
# intro(age="80", name="Arnab"