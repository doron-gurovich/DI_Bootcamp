
// Exercise 1:

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift(); // Remove Banana from the array

fruits.sort(); // Sort the array in alphabetical order.
fruits.push("Kiwi"); // Add “Kiwi” to the end of the array.

console.log(fruits);

fruits = fruits.slice(1); // Remove “Apples” from the array. Don’t use the same method as in part 1.
// delete fruits[0] - the array contain an empty element.

fruits.reverse();// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])

console.log(fruits);

// Exercise 2:

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let strRes = moreFruits[1][1][0];

console.log(strRes);