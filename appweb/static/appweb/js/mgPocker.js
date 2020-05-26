//Fonction changer coleur arrière plan du tag select
function backgroundColor() {
    const colorJetons = ["color0", "color1", "color2", "color3", "color4"];
    for (const element of colorJetons) {
        // console.log(element);
        let colorSelect = $(`#${element}`).val();
        console.log(colorSelect);
        if (colorSelect === "rouge") {
            // console.log(colorSelect);
            $('#' + element).css('background', 'red');
        } else if (colorSelect === "vert") {
            // console.log(colorSelect);
            $('#' + element).css('background', 'green');
        } else if (colorSelect === "orange") {
            // console.log(colorSelect);
            $('#' + element).css('background', 'orange');
        } else if (colorSelect === "bleu") {
            // console.log(colorSelect);
            $('#' + element).css('background', 'blue');
        } else if (colorSelect === "marron") {
            // console.log(colorSelect);
            $('#' + element).css('background', 'brown');
        } else if (colorSelect === "noir") {
            // console.log(colorSelect);
            $('#' + element).css('background', 'black');
        }
    }
}

$(backgroundColor);
// Execution de boucle for les changement de la couleur des jetons
const colorJetons = ["color0", "color1", "color2", "color3", "color4"];
for (const colorJeton of colorJetons) {
    // console.log(colorJeton)
    const selectElement = document.getElementById(colorJeton);
    selectElement.addEventListener('change', () =>  {
        backgroundColor();
    });

}

// fonction temps blinds
function tempsBlind() {
    let tblinds = document.getElementById('tempBlinds').innerHTML; // Récupère la valeur "valeurTemp"
    console.log(tblinds);

}
tempsBlind()
