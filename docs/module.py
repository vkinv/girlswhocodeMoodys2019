#calculator
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def squareroot(x):
    return math.sqrt(x)
def cosine(x):
    return math.cos(x)
def sine(x):
    return math.sin(x)
def tangent(x):
    return math.tan(x)

    


import math

def main():
    while True:
        print("Welcome! This program will allow you to do the basic functions of a calculator.")
        print("Chose a function type: add, subtraction, multiply, divide, squareroot, cosine, sine, tangent.")
        print("Type the first letter of what function you would like. For Squareroot, type sq, and for sine, type si")
        function=input()
        if function== "a":
            num=int(input ("Enter a number "))
            anothernum=int(input ("Enter another number "))
            print("Results:", add(num,anothernum))
        if function=="s":
            num=int(input ("Enter a number"))
            anothernum=int(input ("Enter another number "))
            print("Results:", subtract(num,anothernum))
        if function=="m":
            num=int(input("Enter a number "))
            anothernum=int(input("Enter another number "))
            print("Results:", multiply(num,anothernum))
        if function=="d":
            num=int(input ("Enter a number "))
            anothernum=int(input ("Enter another number "))
            print("Results:", divide(num,anothernum))
        if function=="sq":
            num=int(input ("Enter a number "))
            print("Results:", squareroot(num))
        if function=="c":
            num=int(input ("Enter a number "))
            print("Results:", cosine(num))
        if function=="si":
            num=int(input ("Enter a number "))
            print("Results:", sine(num))
        if function=="t":
            num=int(input ("Enter a number "))
            print("Results:", tangent(num))
main()
