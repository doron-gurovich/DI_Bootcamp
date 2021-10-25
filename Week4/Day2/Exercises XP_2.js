let iAge = Number(prompt("please insert your age", "42"));

function checkDriverAge(num) {
    if(num < 18)  {
        alert("Sorry, you are too young to drive this car. Powering off");
    } else if(num > 18) {
        alert("You are old enough to drive, Powering On. Enjoy the ride!");
    } else if(num === 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    } else {
        console.error("Error: please insert an integer number. \nThe one you gave us is incorrect.");
    }
}

checkDriverAge(iAge);