let strTest = "aqwerty";

CapitalizedLetters = (str) => {
    let arrRes = [];
    let strEven = "even: ";
    let strOdd = "odd: ";

    for(i = 0; i < str.length; i++) {
        if(! ((i + 1)%2) ) {
            strEven += str[i].toUpperCase();
            strOdd += str[i];
        } else {
            strEven += str[i];
            strOdd += str[i].toUpperCase();
        }
    }

    arrRes = [strOdd, strEven, str];

    return arrRes;
}

console.log(CapitalizedLetters(strTest));