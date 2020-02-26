# print
print("Stuff")

# Variables
x = 'stuff'
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
    print("this is happening forever")

# or

x = 5
while x <= 0:
    print("Hi")
    x += 1
