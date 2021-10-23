let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
}

let strName = prompt("Please introduce yourself: ", "Randy, Karla, Wendy, Norman, Sam");
let iFlag = 0;

for (const property in guestList) {

    if(property == strName.toLowerCase()) {
        console.log(`Hi! I'm ${strName}, and I'm from ${guestList[property]}`);
        iFlag++;
        break;
    }
}

if(!iFlag) {

    console.log("Hi! I'm a guest.");
}

// and now lets do it in a better way
/*****
if(strName in guestList === false) {
    console.log(`Hi! I'm ${strName}, and I'm from `); // ${guestList[1]}
} else {
    console.log("Hi! I'm a guest.");
}

 */
