let age = [20,5,12,43,98,55];
let iSum = 0;
let iMax = 0;

for(i = 0; i < age.length; i++) {
    if(age[i] > iMax) {
        iMax = age[i];
    }

    iSum += age[i];
}

console.log("Sum of array elements is equal to: " + iSum);
console.log("Highest age in this array: " + iMax);