// let addressNumber;
// let addressStreet;
// let country;

let globalAddress;

let addressNumber = "9-32";
let addressStreet = "Carmel";
let country = "Israel";
let iLive = "i live in ";

globalAddress = iLive.concat(country, ", ", addressStreet, ": ", addressNumber);

console.log(globalAddress);

let birthdayYear = 1980;
let dateNextYear = new Date().getFullYear()+1;

let myAge = dateNextYear-birthdayYear;

console.log("OMG !!! i will be " + myAge + " in " + dateNextYear);

let pets = ["cat", "dog", "fish", "rabbit", "cow" ];

console.log(pets[1]);
console.log(pets.length);

pets.push("horse");
console.log(pets[5]);

// UI functions

alert("Hello");

let age = prompt('How old are you?', 20);
alert(`You are ${age} years old!`); // You are 20 years old!

let isBoss = confirm("Are you the boss?");
alert(isBoss); // true if OK is pressed
