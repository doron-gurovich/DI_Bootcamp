let arrTest = [[1, 1], [1, 3], [5, 1], [6, 1]]; // [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];

ifOmnipresentValue = (arr, num) => {
    let iTemp = 0;

    for(i = 0; i < arr.length; i++) {
        if(num in arr[i]) {
            iTemp++;
        }
    }

    if(iTemp >= arr.length) {
        return true;
    } else {
        return false;
    }
}

console.log(ifOmnipresentValue(arrTest, 6));