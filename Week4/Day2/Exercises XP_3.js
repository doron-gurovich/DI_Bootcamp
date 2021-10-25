checkNumbers = () => {

    let i = 0;

    while(i++ < 100) {
        if(!(i%2)) {
            console.log(`the number ${i} is even`);
        } else {
            console.log(`the number ${i} is odd`);
        }
    }
}

checkNumbers();