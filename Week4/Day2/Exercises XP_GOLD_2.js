let strFullName = "Robin Singh";

abbrevName = (str) => {
    let arr = str.split(" ");
    
    arr[arr.length - 1] = arr[arr.length - 1][0] + ".";

    return arr.join(' ');
}

console.log(abbrevName(strFullName));