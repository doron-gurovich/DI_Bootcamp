let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
var strResult = NaN;

switch(users.length) {
    case 0:
        strResult = "no one is online";
        break;
    case 1:
        strResult = `${users[0]} is online`;
        break;
    case 2:
        strResult = `${users[0]} and ${users[1]} are online`;
        break;
    default:
        strResult = `${users[0]}, ${users[1]}, and ${users.length - 2} more are online`;
        break;
}

alert(strResult);