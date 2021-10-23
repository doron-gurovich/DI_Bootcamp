let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let strRes = "";

names = names.sort();

for(i = 0; i < names.length; i++) {
    strRes += names[i][0];
}

console.log(strRes);