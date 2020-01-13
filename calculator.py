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

def square(a):
	return a*a

def cube(a):
	return a*a*a

def square_n_times(a, n):
	return a**n


#ask user input
a = eval(input("Enter the first number: "))
o = str(input("Enter the operation (+, -, *, /, square, cube, n-squares): "))
if o =="n-squares":
	n = eval(input("Enter the n: "))
elif o != "square" and o!= "cube":
	b = eval(input("Enter the second number: "))


#print explanations of the calculator

if o == "*":
	print("I'm using the calculator functions to multiply " + str(a) + " and " + str(b))
	x = multiply(a,b)
	print(x)

if o == "+" :
	print("I'm using the calculator functions to add " + str(a) + " and " + str(b))
	x = add(a,b)
	print(x)

if o == "-":
	print("I'm using the calculator functions to subtract " + str(a) + " from " + str(b))
	x = subtract(a,b)
	print(x)

if o == "/":
	print("I'm using the calculator functions to divide " + str(a) + " by " + str(b))
	x = divide(a,b)
	print(x)

if o == "square":
	print("I'm using the calculator functions to find the square of " + str(a))
	x = square(a)
	print(x)

if o == "cube":
	print("I'm using the calculator functions to find the cube of " + str(a))
	x = cube(a)
	print(x)

if o == "n-squares":
	print("I'm using the calculator functions to square the number " + str(a) 
		+ " " + str(n)+ " times.")
	x = square_n_times(a, n)
	print(x)









