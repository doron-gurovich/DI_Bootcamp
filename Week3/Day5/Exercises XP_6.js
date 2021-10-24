let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}

let strDetails = "";

for(i = 0; i < Object.keys(details).length; i++) {
    strDetails += Object.keys(details)[i] + " " + Object.values(details)[i] + " ";
} // JSON.stringify is another option here 

console.log(strDetails);