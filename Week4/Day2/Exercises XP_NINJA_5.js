const arrTest = [1,2,3,3,3,3,4,5,1,0,-1];

uniqueElements = (arr) => {
    let arrTemp = arr.slice().sort();
    let arrRes = [];

    for(i = 0; i < arr.length; i++) {
        if(arrTemp[i] != arrTemp[i+1]) {
            arrRes.push(arrTemp[i]);
        }
    }

    return arrRes;
}

console.log(`check this out! \nWe took ${arrTest} \nand transform it to ${uniqueElements(arrTest)}`);