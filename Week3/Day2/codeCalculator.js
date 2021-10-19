/*

Exercises #3, Calculator

https://stackoverflow.com/questions/69622095/function-definition-in-js-simple-calculator

*/ 

var numRes = NaN;
var num1 = Number(prompt("please enter the first number", "12"));
var num2 = Number(prompt("please enter the second number", "21"));
var strOperator = prompt("please enter the operator (+, -, *, /)", "+");

/*

this is an old version. works but not elegant.

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
*/

var calc = {
    '+': function (x, y) { return x + y; },
    '-': function (x, y) { return x - y; },
    '*': function (x, y) { return x * y; },
    '/': function (x, y) { return x / y; }
};

if(calc.hasOwnProperty(strOperator)) {
    if(calc.hasOwnProperty('-') && (num2 == 0)) {
        numRes = "ERROR div by zero";
    } else if (isNaN(num1) || isNaN(num2)) {
        numRes = "ERROR no numbers was found";
    } else {
        numRes = calc[strOperator](num1, num2);
    }
} else {
    numRes = "ERROR incorrect operator";
}

if(isNaN(numRes)) {
    numRes = "ERROR some undefined error here";
}

alert("The result is following: " + numRes);