var intGrade = Number(prompt("please define your grade:", "95"));

function funcGrade (int) {
    if(int > 90) {
        return "A";
    } else if(int > 80 && int <= 90) {
        return "B";
    } else if(int >= 70 && int <= 80) {
        return "C";
    } else if(int < 70) {
        return "D";
    } else {
        return "Sorry, this grade was not defined";
    }
}

alert(funcGrade(intGrade));