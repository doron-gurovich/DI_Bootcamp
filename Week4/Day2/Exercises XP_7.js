let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppingList = {
    "banana": 1,
    "orange": 1,
    "apple": 2
}

myBill = () => {

    let iSum = 0;

    for(i = 0; i < Object.keys(shoppingList).length; i++) {
        for(j = 0; j < Object.keys(prices).length; j++) {
            if(Object.keys(shoppingList)[i] === Object.keys(prices)[j]) {
                for(k = 0; k < Object.keys(stock).length; k++) {

                    if(Object.keys(shoppingList)[i] === Object.keys(stock)[k]) {
                        if(Object.values(stock)[k] >= Object.values(shoppingList)[i] ) {
                            iSum += Object.values(shoppingList)[i] * Object.values(prices)[j];
                            Object.values(stock)[k] -= Object.values(shoppingList)[i];

                        } else {
                            alert(`Sorry, the item you have in the list ${Object.keys(shoppingList)[i]} is not available now. Come back late`);
                        }
                    }
                }
            }
        }
    }

    console.log(`The total price is : ${iSum}`)
}

myBill();