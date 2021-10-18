//Exercise 3 : Calculator

var num1 = Number(prompt("please enter the first number"));
var num2 = Number(prompt("please enter the second number"));
var strOperator = prompt("please enter the operator (+, -, *, /)");

var numRes = NaN;

/*

https://stackoverflow.com/questions/69622095/function-definition-in-js-simple-calculator

var calc = {
    '+': function (x, y) { return x + y; },
    '-': function (x, y) { return x - y; }
}​​​​​​​;
*/

if(strOperator.localeCompare("+")==0) {
    numRes = num1 + num2;
} else if(strOperator.localeCompare("-")==0) {
    numRes = num1 - num2;
} else if(strOperator.localeCompare("*")==0) {
    numRes = num1 * num2;
} else if(strOperator.localeCompare("/")==0 && (num2 != 0) ) {
    numRes = num1 / num2;
} else {
    numRes = "error: no operator was found";
}

alert("result is following: " + numRes);