var strVerb = prompt("Prompt the user for a string. It must be a verb.", "swiming");
var strResult = NaN;
var strEnd = "";

for(i = 1; i <= 3; i++) {
    strEnd += strVerb.charAt(strVerb.length-i);
}

strEnd = strEnd.split("").reverse().join(""); // reverse this string

if (strVerb.length <= 3) {
    strResult = strVerb
} else if(strEnd.localeCompare("ing")) {
    strResult = strVerb.concat("ing");
} else {
    strResult = strVerb.concat("ly");
}

alert(strResult);