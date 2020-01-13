#!/usr/bin/env python3

# four functions

def multiply(a,b):
	return a*b

def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def divide(a,b):
	return a/b


#ask user input
a = eval(input("Enter the first number: "))
o = str(input("Enter the operation: "))
b = eval(input("Enter the second number: "))

#print explanations of the calculator

if o == "*":
	print("I'm going use the calculator functions to multiply " + str(a) + " and " + str(b))
	x = multiply(a,b)
	print(x)

if o == "+" :
	print("I'm going use the calculator functions to add " + str(a) + " and " + str(b))
	x = add(a,b)
	print(x)

if o == "-":
	print("I'm going use the calculator functions to subtract " + str(a) + " from " + str(b))
	x = subtract(a,b)
	print(x)

if o == "/":
	print("I'm going use the calculator functions to divide " + str(a) + " and " + str(b))
	x = divide(a,b)
	print(x)
