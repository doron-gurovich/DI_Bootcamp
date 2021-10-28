let iNum = Number(prompt("Please insert some integer number in range (0, 99)", "99"));
let arrResult = [];

let iCurrentNumOfBottles = iNum;
let iDelta = 1;
let i = 0;
let strItThem = "it";

// here we will form first / last strings of array

arrResult[i++] = "==============================";

while(iCurrentNumOfBottles > iDelta) {

    strItThem = (iDelta == 1 ? "it" : "them");

    let strTemp = `${iCurrentNumOfBottles} bottles of beer`;

    arrResult[i++] = strTemp + ` on the wall \n`;
    arrResult[i++] = strTemp + `\n`;
    arrResult[i++] = `Take ${iDelta} down, pass ${strItThem} around \n`;

    iCurrentNumOfBottles -= iDelta++;
}

arrResult[i++] = `${iCurrentNumOfBottles} bottles of beer on the wall \n`;
arrResult[i] = "==============================";

// lets print the result now w/ console.log()

for(j = 0; j < arrResult.length; j++) {
    console.log(arrResult[j]);
}