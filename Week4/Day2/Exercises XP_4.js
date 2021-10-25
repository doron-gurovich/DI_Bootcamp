let iBillAmount = Number(prompt("please insert the amount of the bill", "120"));

tipCalculatorByJohn = (num) => {
    if(num < 50) {
        return num * 0.2;
    } else if(num >= 50 && num <= 200) {
        return num * 0.15;
    } else if(num > 200) {
        return num * 0.1;
    } else {
        console.error("incorrect amount has been inserted. \nPlease review.");
        return -1;
    }
}

alert(`congratulation John! \nTip amount is ${tipCalculatorByJohn(iBillAmount)}, \nFinal bill (bill + tip) is ${iBillAmount+tipCalculatorByJohn(iBillAmount)}`);