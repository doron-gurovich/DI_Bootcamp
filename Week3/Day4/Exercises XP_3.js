var intUserNum = Number(prompt("please insert some integer number", "5"));
var strResult = NaN;

if(intUserNum%2 == 0) {
    strResult = "x is an even number";
} else {
    strResult = "x is an odd number";
}

alert(strResult);