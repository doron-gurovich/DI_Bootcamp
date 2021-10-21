var strSentence = prompt("insert the tested string. need to include not ... bad", "The movie is not that bad, I like it");
var strResult = strSentence;

function funParcer(str) {

    var iNot = (str.toLowerCase()).indexOf("not");
    var iBad = (str.toLowerCase()).indexOf("bad");

    if(iNot == -1 && iBad == -1) {
        return "the sentence you provide us doesn't contain 'not' or 'bad'";
    } else if(iBad < iNot && iBad != -1) { // If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
        return str;
    } else if(iBad > iNot && iNot!= -1) { // If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
        return str.replace(str.substr(iNot, (iBad + 3 - iNot)), "good");
    } else if(iBad < iNot && iBad == -1) { // i dont really understand what the question here ? what do you expect as an output ? its probably the same substr(), but from where we met 'not' till the end of the sentence ?
        return str.substr(0, iNot);
    } else if(iBad > iNot && iNot == -1) { // same question as the one above ... here i left the second part of the sentence. all after 'bad' (included)
        return str.substr(iBad + 3);
    }
}

console.log("output for your sentence (" + strSentence + ") is: \n" + funParcer(strSentence));