# print
print("Hello world")

# Variables
x = 'string'
print(x)

# lists
fruits = ['apple', 'banana', 'orange']
print("The 0th entry in fruits is", fruits[0])
print("fruits is", fruits)
fruits.append('pomagranate')
print("fruits in now", fruits)

# Conditional statements
myBool = True
if myBool == True:
  print("My boolean variable is true")
elif myBool == False:
  print("My boolean variable is false.")
else:
  print("Oops")

# Input
name = input("What is your name?")
age = float(input("How old are you"))
info = [name, age]

# sleep
import time
print("this happened")
time.sleep(1)
print("this happened a second later")
# or
from time import *
print("hi")
sleep(1)
print("bye")


# Loops
import time
fruits = ["apple", "banana", "pear"]
for fruit in fruits:
    print("one of my fruits is")
    print(fruit)
    time.sleep(1)

# while
while True:
    print("this is not happening forever")
    break
# or

x = 5
while x <= 0:
    print("Hi")
    x += 1

# For
from time import *
fruits = ["apple", "banana", "pear"]
for fruit in fruits:
  print(fruit)
  sleep(1)

# range
max = int(input("Up to what number would you like to square?"))
for i in range(max + 1):
  print("The square of", i, "is", i ** 2)

# Functions
# w/o arguments
def myFunction():
    print("Hello from a function!")
for i in range(10):
    myFunction()

# w/ arguments
def square(x):
    x = x ** 2
    return x

print(square(16))

def printSquares(max):
    for i in range(max):
      print("The square of", i, "is", i ** 2)

printSquares(12)

# Factor function for students

def factor(x):
    factors = []
    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)
    return factors
print(factor(24))
