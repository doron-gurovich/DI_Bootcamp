var v1 = [(5 + "34"), (5 - "4"), (10 % 5), (5 % 10), ("Java" + "Script"), (" " + " "), (" " + 0), true + true, true + false, false + true, false - true, 3 - 4, "Bob" - "bill"];

var v1Results = ["string", "int, 1", "Modulus (Remainder)", "Modulus (Remainder)", "string", "string", "string", "bool, 2","bool, 1", "bool, 1", "bool, -1","-1", "mistake"];

console.log(v1);
console.log(v1Results);

// Exercises XP Gold

// Exercise 1 : Favorite Color
let me = ["my","favorite","color","is","blue"];
var strMe = me.join(' ');
console.log(strMe);

// Exercise 2 : Mixup

let str1 = "mix";
let str2 = "pod";

/*
var temp = str2[1];
str2[1] = str2[0];
str2[0] = temp;
*/

var arrStr2 = str2.split('');
arrStr2[0] = arrStr2.splice(1, 1, arrStr2[0])[0];
str2MIX = arrStr2.join('');

var str3 = str1.concat(' ', str2);

console.log(str3);

//Exercise 3 : Calculator

var num1 = Number(prompt("please enter the first number"));
var num2 = Number(prompt("please enter the second number"));
var strOperator = prompt("please enter the operator");

/*
var math_it_up = {
    '+': function (x, y) { return x + y; },
    '-': function (x, y) { return x - y; }
};​​​​​​​
*/
var numRes = 0; // math_it_up['+'](num1, num2);

alert(numRes);

// Exercises XP Ninja

// Exercise 1 : Find Nemo

var strNemo = prompt("please introduce Nemo");
var intNemo = strNemo.indexOf("Nemo");

if (intNemo<0) {
    alert("your string doesnt contain Nemo");
} else {
    alert(intNemo);
}

// Exercise 3 : Ask For Numbers

var strNumbers = prompt("please insert the string of numbers separated by commas. we will calculate the sum", "1,2,3,4,5,6,7,8,9");
var arrNumbers = strNumbers.split(',');

var sum = 0;
let i = 0;

while(i<arrNumbers.length) {
    sum+= Number(arrNumbers[i++]);
}

alert("calculations results: " + sum);

// Exercise 4 : Boom

var exe4Input = Number(prompt("please insert the int number"));

if (exe4Input < 2) {
    alert("boom!");
}8