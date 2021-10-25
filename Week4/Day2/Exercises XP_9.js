const hotelPricePerNight = 140;
const objLocation = {
    "London" : 183,
    "Paris" : 220,
    "All other destination" : 300
}
const carCostDaily = 40;

hotelCost = (num = hotelPricePerNight) => {
    
    let numOfNights = NaN;
    
    while(isNaN(numOfNights) || numOfNights === 0) {
        numOfNights = Number(prompt("please define the number of nights you gonna stay", "3"));
    }

    return num * numOfNights;
}

planeRideCost = (obj = objLocation) => {
    let strDestination = "";

    while(! (strDestination in obj) ) {
        strDestination = prompt("define your destination", "London, Paris, All other destination");
    }

    for(i = 0; i < Object.keys(obj).length; i++) {
        if(strDestination === Object.keys(obj)[i]) {
            return Object.values(obj)[i];
        }
    }
}

rentalCarCost = (num = carCostDaily) => {
    let numOfDays = NaN;
    let rentalCarPriceWithDiscount = 0.1;
    
    while(isNaN(numOfDays) || numOfDays === 0) {
        numOfDays = Number(prompt("please define the number of days you gonna stay", "4"));
    }

    if(numOfDays > 10) {
        return rentalCarPriceWithDiscount *= (num * numOfDays);
    } else {
        return num * numOfDays;
    }
}

totalVacationCost = () => {
    
    return hotelCost() + planeRideCost() + rentalCarCost();
}

console.log(totalVacationCost());