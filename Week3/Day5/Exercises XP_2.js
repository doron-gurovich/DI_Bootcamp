let people = ["Greg", "Mary", "Devon", "James"];

people.push("Doron");

for(i = 0; i < people.length; i++) {
    if(people[i] === "Greg") {
        people.splice(i, 1);
    } else if(people[i] === "James") {
        people[i] = "Jason";
    }
}

// printing loop

people.forEach((element, index) => {
    console.log(element, index)
});

for(let element of people) {
    console.log(element);
    if(element === "Jason") {
        break;
    }
}

// copy of people array

let peopleCopiedWithSlice = people.slice(0); // assuming that we know "Mary" index (== 0) from the begining, we could apply people.slice(1)

peopleCopiedWithSlice.forEach((element, index) => {
    if(element === "Mary") {
        peopleCopiedWithSlice.splice(index, 1);
    }
});

// Here we are. LEts take Mary's index :)
// for ( ... ) {... people[i] === "Mary" ... } is a trivial solution here

console.log(people.indexOf("Mary"));

console.log(people.indexOf("Foo")); // people doesnt contain Foo ... 

let last = people[people.length - 1]; // the last but not the least :))