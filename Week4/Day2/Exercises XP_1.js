function infoAboutMe() {
    console.log("my name is Doron. I'm living in Rehovot.");
}

infoAboutMe();

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`Your name is ${personName}, your are ${personAge} years old, and your favorite color is ${personFavoriteColor}.`);
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

function infoAboutPersonPart3(personName, personAge, personFavoriteColor, personHobbies) {

    infoAboutPerson(personName, personAge, personFavoriteColor);

    personHobbies.forEach((element, index) => {
        console.log(`hobbie # ${index} is ${element}`);
    });
}

infoAboutPersonPart3("David", 45, "blue", ["tennis", "painting"]);
infoAboutPersonPart3("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"]);