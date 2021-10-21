var strSecretWord = prompt("please insert some word", "Hello world!");
var strCommand = prompt("please insert the action", "remove, replace");

function funcVowels (str, command) {
    var pattern = /[aeiouy]/g;
    var arrPattern = ['a','e','i','o','u','y'];
    var arrReplace = ['1','2','3','4','5','6'];

    if(!command.localeCompare("remove")) {
        return str.replace(pattern, '');
    } else if(!command.localeCompare("replace")) {
        
        for(i = 0; i < str.length; i++) { // brutal force solution ... 
            for(j = 0; j < arrPattern.length; j++) {
                if(!str[i].localeCompare(arrPattern[j])) {
                    str = str.replace(str[i], arrReplace[j]); 
                }
            }
        }

        return str;
        
    } else {
        return "command is incorrect";
    }
}

alert("result of vowels removing from (" + strSecretWord + ") is " + funcVowels(strSecretWord, strCommand));

