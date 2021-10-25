let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

checkBasket = (obj) => {
    let strProp = prompt("please insert the item", "floss");

    if(strProp in obj) {
        alert(`yes, your item ${strProp} is in the besket!`);
    } else {
        alert(`Unfortunately your item ${strProp} is not in the besket!`);
    }
}

checkBasket(amazonBasket);