let iRandom = Math.random() * 100;
let strRes = "the list of even numbers: "

for(i = 0; i < iRandom; i++) {
    if(! (i%2) ) {
        strRes += i;
    }

    strRes += " ";
}

console.log(`random number ${iRandom} gave us ${strRes}`);