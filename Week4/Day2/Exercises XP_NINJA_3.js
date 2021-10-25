const strTest = "Madam";

isPalindrome = (str) => {
    let strTemp = str.slice().toLowerCase();
    let iLength = strTemp.length - 1;

    for(i = 0; i < Math.trunc(strTemp.length); i++) {
        if(strTemp[i] != strTemp[iLength - i] ) {
            return false;
        }
    }

    return true;
}

console.log(`the string ${strTest} is palindrome: ${isPalindrome(strTest)}`);