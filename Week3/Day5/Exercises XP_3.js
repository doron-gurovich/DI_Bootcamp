let iNumber = NaN

while(iNumber != 10) {
    iNumber = Number(prompt("please insert some integer number", "10"));

    if(isNaN(iNumber)) {
        alert("that wasn't a number. try harder!");
    } else if(iNumber != 10) {
        alert("Your number not yet there. try harder!");
    } else {
        alert("You did it! Great job!");
    }
}