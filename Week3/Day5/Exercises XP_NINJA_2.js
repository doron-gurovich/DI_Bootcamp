let strGradesList = prompt("please insert the array", "20,5,12,43,98,55");

let iGradesList = strGradesList.split(',').map(Number);
let strCreteria = "";
let iResult = 0;


/**
let iGradesList = strGradesList.split(',').map(function(item) {
    return parseInt(item, 10);
});

 */


function findAvg(arr) {
    let iSum = 0;
    let iResult = 0;

    for(i = 0; i < arr.length; i++) {
        iSum += arr[i];
    }

    iResult = iSum / arr.length;

    // console.log("AVG of array's elements is: ", iResult); -- i could do it as requested. i think better to organize output outside of the AVG function
    return iResult;
}


function gradeOutput(num) {
    if(num > 65) {
        console.log(`Well done! you passed with grade ${num}`);
    } else {
        console.log(`Your result ${num} could be better! Lets try again`);
    }
}

// and now execution

gradeOutput(findAvg(iGradesList));