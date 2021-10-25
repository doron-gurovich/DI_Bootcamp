let divisor = Number(prompt("please insert the divisor", "23"));

isDivisible = (num = 23) => {

    let j = 0;
    let arrResults = [];

    for(i = 0; i < 500; i++) {
        if(!(i%num)) {
            arrResults[j++] = i;
        }
    }

    console.log(`Outcome: ${arrResults} \nSum: ${arrResults.reduce((a, b) => a+b, 0)}`);

}

isDivisible(divisor);