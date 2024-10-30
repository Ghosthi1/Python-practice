import calendar

print('hello world')

def greet(name):
    print('greetings ' + name)

name = input("Enter name ")
greet(name)

def printCallender():
    cal = calendar.month(2024, 2)
    print(cal)