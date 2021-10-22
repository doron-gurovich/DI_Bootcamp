let names= ["john", "sarah", 23, "Rudolf",34];

for(i = 0; i < names.length; i++) {
    if(typeof names[i] === 'string'){
        
        if(names[i][0] == names[i][0].toUpperCase()) {
            console.log("this is string " + " " + names[i]+ " " + i);
            continue;  
        } else {
            console.log("this is string " + i);
        }

    } else continue;
}

for(i = 0; i < names.length; i++) {
    if(typeof names[i] === 'string'){
        console.log("this is string " + names[i]);
    } else break;
}