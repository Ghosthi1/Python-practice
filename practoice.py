import calendar
import random

def Hello():
    print('hello world')

    def greet(name):
        print('greetings ' + name)

    name = input("Enter name ")
    greet(name)

def printCallender():
    cal = calendar.month(2024, 2)
    print(cal)

def randomInt(x,y):
    number = random.randint(x,y)
    print(number)

def ranMovie():
    movies = ["alladin","avrage avengers", 'endme']
    print(random.choice(movies))
    
function = input("What function ")

match function:
    case "Hello":
        Hello()
    case "Callender":
        printCallender()
    case "random range":
        min = input("Please enter min value ")
        max = input("Please endter max value ")
        randomInt(min,max)
    case "Movie":
        ranMovie()



