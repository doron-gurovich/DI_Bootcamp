let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

console.log("number of floors in the building: " + building.numberOfFloors);

console.log("how many appartments are on the first floor: " + building.numberOfAptByFloor.firstFloor);
console.log("how many appartments are on the second floor: " + building.numberOfAptByFloor.secondFloor);
console.log("how many appartments are on the third floor: " + building.numberOfAptByFloor.thirdFloor);

let strNameDan = building.nameOfTenants[1];
console.log("name of the second tenant and the number of rooms he has in his apartment: " + strNameDan, building.numberOfRoomsAndRent.dan[0]);

let iSarah = building.numberOfRoomsAndRent.sarah[1];
let iDan = building.numberOfRoomsAndRent.dan[1];
let iDavid = building.numberOfRoomsAndRent.david[1];

if(iSarah + iDavid > iDan) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}