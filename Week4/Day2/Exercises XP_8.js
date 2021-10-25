const theItemPrice = .75;
let arrChange = [0, 0, 20, 5];
const objRatio = {
    "quaters" : 0.25,
    "dimes" : 0.1,
    "nickel" : 0.05,
    "penny" : 0.01
};

changeEnough = (num, arr) => {
    let iSum = 0;
    let boolRes = false;

    arr.forEach((element, index) => {
        iSum += element * Object.values(objRatio)[index];
    });

    if(iSum >= num) {
        boolRes = true;
    }

    return boolRes;
}

console.log(changeEnough(theItemPrice, arrChange));