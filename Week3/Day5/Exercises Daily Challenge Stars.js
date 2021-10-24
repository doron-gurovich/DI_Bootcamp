let star = prompt("define the Star", "*");
let iNum = Number(prompt("define the number of lines", "5"));

star += " ";
let strLine = "";

for(i = 0; i < iNum; i++) {
   for(j = 0; j <= i; j++) {
        strLine += star;
    }

    console.log(strLine);
    strLine = ""; // this plastir (strLine) came from the sad fact that i didnt manage to exclude \n from console.log(). stream.stdout.write() doesnt work for not et clear reasons
}