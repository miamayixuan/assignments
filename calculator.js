function multiply(a,b) {
	return a*b
}

function add(a,b) {
	return a+b
}

function subtract(a,b) {
	return a-b
}

function divide(a,b) {
	return a/b
}

const prompt = require('prompt-sync')()

var a = prompt('Enter the first number: ')
var operation = prompt('Enter the operation (+, -, *, /): ');
var b = prompt('Enter the second number: ');

if (operation == "*") {
	console.log("I'm going use the calculator functions to multiply " + a +
		" and  " + b)
	var x = multiply(a,b)
	console.log(x)
}

if (operation == "+") {
	console.log("I'm going use the calculator functions to add " + a +
		" and  " + b)
	var x = add(a,b)
	console.log(x)
}

if (operation == "-") {
	console.log("I'm going use the calculator functions to subtract " + a +
		" from  " + b)
	var x = subtract(a,b)
	console.log(x)
}

if (operation == "/") {
	console.log("I'm going use the calculator functions to divide " + a +
		" by  " + b)
	var x = divide(a,b)
	console.log(x)
}