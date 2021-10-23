let numbers = [123, 8409, 100053, 333333333, 7];

for(i = 0; i < numbers.length; i++) {
        console.log(numbers[i] + " Divisible by three? " +!Boolean(numbers[i]%3));
}