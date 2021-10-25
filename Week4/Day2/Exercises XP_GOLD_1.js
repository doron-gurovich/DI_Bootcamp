isStringBlank = (str) => {
    if(!str.length) {
        return true;
    } else {
        return false;
    }
}

console.log(isStringBlank(''));