var newDog = "Chihuahua";

var intLenghOfNewDog = newDog.length;

console.log("how many letters are in newDog? : " + intLenghOfNewDog);

console.log(newDog.toUpperCase(), newDog.toLowerCase());

if(!newDog.localeCompare("Chihuahua")) {
    console.log("I love Chihuahuas, it's my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}