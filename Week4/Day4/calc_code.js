function myFunction() {
    var x = document.getElementById("myBtn").value;
    document.getElementById("demo").innerHTML = x;
}


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