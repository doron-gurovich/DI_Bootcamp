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

var math_it_up = {
    '+': function (x, y) { return x + y; },
    '-': function (x, y) { return x - y; }
};​​​​​​​

var numRes = 0; // math_it_up['+'](num1, num2);

alert(numRes);