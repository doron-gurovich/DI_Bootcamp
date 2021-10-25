let objOld = {
    FullName: "Qwe",
    Mass: 130,
    Hieght: 190,

    BMI_calc: function() {
        return this.Mass / (Math.pow(this.Hieght, 2));
    }
}

let objNew = {
    FullName: "Asd",
    Mass: 120,
    Hieght: 190,

    BMI_calc: function() {
        return this.Mass / (Math.pow(this.Hieght, 2));
    }
}

function compateBMI(obj1, obj2) {
    if(obj1.BMI_calc() > obj2.BMI_calc()) {
        return `${obj1.FullName} BMI is higher`;
    } else {
        return `${obj2.FullName} BMI is higher`;
    }
}

console.log(compateBMI(objOld, objNew))