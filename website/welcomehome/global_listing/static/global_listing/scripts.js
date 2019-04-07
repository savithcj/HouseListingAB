function getFloorType(typeAsInt, id){

    let type = "";

    switch (typeAsInt) {
        case 0:
            type = "Carpet";
            break;
        case 1:
            type = "Laminated";
            break;
        case 2:
            type = "Hard Wood";
            break;
        case 3:
            type = "Wood/Polymer Composite";
            break;
        case 4:
            type = "Vinyl";
            break;
        case 5:
            type = "Painted/Epoxy";
            break;
        case 6:
            type = "Unfinished Concrete";
            break;
        case 7:
            type = "Other";
    }

    document.getElementById(id).innerHTML = type;
}


function getShapeType(typeAsInt, id){

    let type = "";

    switch (typeAsInt) {
        case 0:
            type = "Square/Rectangle";
            break;
        case 1:
            type = "Round";
            break;
        case 2:
            type = "Irregular";
            break;
        case 3:
            type = "Other";
    }

    document.getElementById(id).innerHTML = type;
}