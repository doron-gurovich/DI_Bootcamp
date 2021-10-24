var strSentence = prompt("please insert a few words divided by commas ", "Teacher, is, always, cheating, us, when, he, saying, he, is, a stupid., We, ALL, know, he, is, good!");

const arrStrSentence = strSentence.split(",");

function addStars(arr) {
    // define the length of the longest world inthe array
    let iMaxLength = arr[0].length;

    for(i = 1; i < arr.length; i++) {
        if(iMaxLength < arr[i].length) {
            iMaxLength = arr[i].length;
        }
    }

    // adding stars
    // first we create the first/ last string
    let arrRes = [];
    
    arrRes[0] = "";
    arrRes[(arr.length+1)] = "";
    iMaxLength += 4; // 4 here is some number we used. 2x spaces and 2x stars

    for(i = 0; i <= iMaxLength; i++) {
        arrRes[0] += "*";            // this is our first string
        arrRes[arr.length+1] += "*"; // this is our last string
    }

    for(i = 1; i <= arr.length; i++) {
        arrRes[i] = "* " + arr[i-1];

        for(j = arrRes[i].length; j < iMaxLength; j++ ) {
            arrRes[i] += " ";
        }

        arrRes[i] += "*";
    }
    
    return arrRes;
}

let arrResult = addStars(arrStrSentence);

for(i = 0; i < arrResult.length; i++) {
    console.log(arrResult[i]);
}