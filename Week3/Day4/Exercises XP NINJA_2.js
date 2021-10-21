var strZipCode = prompt("please insert your zip code", "70537");
var intZipNum = 5;

function funNoRE (str, num) {
    if(str.length == num) {
        if(!Number.isNaN(parseInt(str, 10))) {
            return "{success} your zip code (" + str + ") is correct";
        } else {
            return "{error} your zip code (" + str + ") is wrong: contains some prohibited symbols"
        }
    } else {
        return "{error} your zip code (" + str + ") is wrong: less/more then 5x symbols"
    }
}

alert("funNoRE result is: " + funNoRE(strZipCode, intZipNum));

function funRE (str, num) {
    
    var pattern = /[0-9]/g;
    var arr = str.match(pattern);

    if(arr === null || (arr.length != num)) {
        return "{error} your zip code (" + str + ") is wrong.";
    } else {
        return "{success} your zip code (" + str + ") is correct.";
    }
}

alert("funRE result is: " + funRE(strZipCode, intZipNum));