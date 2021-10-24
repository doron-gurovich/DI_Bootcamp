const numbers = [5,0,9,1,7,4,2,6,3,8];

let strToString = numbers.toString();
let strJoin = numbers.join(" + ");

let temp = 0;

for(i = 0; i < numbers.length; i++) {
    for(j = i; j < numbers.length; j++) {
        if(numbers[i] < numbers[j]) {
            temp = numbers[i];
            numbers[i] = numbers[j];
            numbers[j] = temp;
        }
    }
}