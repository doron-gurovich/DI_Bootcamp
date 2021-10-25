let arrTest = ['a', 3, 4, 2];


biggestNumberInArray = (arrayNumber) => {
    let iResult = 0;
    
    for(i = 0; i < arrayNumber.length; i++) {
        if(arrayNumber[i] > iResult) {
            iResult = arrayNumber[i];
        }
    }
    
    return iResult;
}

console.log(`we found that in the array ${arrTest} \nThe biggest number is ${biggestNumberInArray(arrTest)}`);