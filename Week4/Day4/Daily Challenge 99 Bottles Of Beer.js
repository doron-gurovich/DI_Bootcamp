const iNum = parseInt(prompt("Please insert some integer number in range (0, 99)", "99")); // parceInt() is better then Number() : https://thisthat.dev/number-constructor-vs-parse-int/

let arrResult = [];
let iCurrentNumOfBottles = iNum;
let iDelta = 1;
let strItThem = "it";

// here we will form first / last strings of array

arrResult.push("==============================");

while(iCurrentNumOfBottles >= iDelta) {

    strItThem = (iDelta == 1 ? "it" : "them");

    let strTemp = `${iCurrentNumOfBottles} bottles of beer`;

    arrResult.push(`${strTemp} on the wall \n`);
    arrResult.push(`${strTemp} \n`);
    arrResult.push(`Take ${iDelta} down, pass ${strItThem} around \n`);

    iCurrentNumOfBottles -= iDelta++;
}

arrResult.push(`${iCurrentNumOfBottles} bottles of beer on the wall \n`);
arrResult.push("==============================");

// lets print the result now w/ console.log()

for(let j = 0; j < arrResult.length; j++) {
    console.log(arrResult[j]);
}