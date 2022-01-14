#this quiz will get better over time
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#code start down here
print('Hello there!')
time.sleep(1)
cls()
print('My name is Indev!')
time.sleep(1)
name = input("What's your name? : ")
cls()
time.sleep(1)
print('Hello! ' + name)
time.sleep(1)
cls()
time.sleep(1)
print("I have some quiz for you! \neach correct answer, I'll give you one points!")
time.sleep(1)
cls()
print("For my first question is!")
point = 0
print("What's 1+1?")
print("1. 2 \n2. 3 \n3. 6 \n4. 69420")
answer = input('type your answer: ')
if answer == "1":
    print('Correct! \n You got 1 point!')
    point + 1
else:
    print('Wrong!')
