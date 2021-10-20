var strWhichLanguage = prompt("Which language do you speak?", "English, Hebrew, French");
var strResult = NaN;

var objGreetings = {
    Language: ["english", "hebrew", "french"],
    Greetings: ["Hello", "Shalom", "Bonjour"]
}

strWhichLanguage = strWhichLanguage.toLowerCase();

for (let i = 0; i < objGreetings.Language.length; i++) {
    if(!strWhichLanguage.localeCompare(objGreetings.Language[i])) {
        strResult = objGreetings.Greetings[i];
        break;
    } else {
        strResult = "Sorry, this language is not yet define";
    }
}

alert(strResult);