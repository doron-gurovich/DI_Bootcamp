let family = {
    parent: ["mom", "dad"],
    kids: ["girl", "boy"],
    budjet : 100
}

for(i = 0; i < Object.keys(family).length; i++) {
    console.log(Object.keys(family)[i]);
}

for(i = 0; i < Object.values(family).length; i++) {
    console.log(Object.values(family)[i]);
}