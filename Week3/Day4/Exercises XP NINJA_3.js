var strSecretWord = prompt("please insert some word", "Hello world!");
var strCommand = prompt("please insert the action", "remove, replace");

function funcVowels (str, command) {
    var pattern = /[aeiouy]/g;
    var arrReplace = ['1','2','3','4','5','6'];

    if(!command.localeCompare("remove")) {
        return str.replace(pattern, '');
    } else if(!command.localeCompare("replace")) {
        
        for(i = 0; i < str.length; i++) {
            if(pattern.test(str[i])) {
                str = str.replace(pattern, arrReplace[i]); // not yet working properly
            }    
        }

        return str;
        
    } else {
        return "command is incorrect";
    }
}

alert("result of vowels removing from (" + strSecretWord + ") is " + funcVowels(strSecretWord, strCommand));

