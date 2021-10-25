let strInput = "The Quick Brown Fox";

strSwapCase = (str) => {
    let strRes = "";
    let strTemp = "";
    let arrStr = str.split(" ");

    for(i = 0; i < arrStr.length; i++) {
        for(j = 0; j < arrStr[i].length; j++) {
            if(arrStr[i][j] == arrStr[i][j].toUpperCase()) {
                strTemp = arrStr[i][j].toLowerCase();
            } else {
                strTemp = arrStr[i][j].toUpperCase();
            }
            strRes += strTemp;
        }

        strRes += " ";
    }
    return strRes;
}

console.log(`SwapCase() results \n${strInput} --> ${strSwapCase(strInput)}.`);