//Fonction changer coleur arrière plan du tag select
function bgcolor() {
    let colorSelect0 = $('#color0').val();
    if (colorSelect0 === "rouge") {
        console.log(colorSelect0);
        $('#color0').css('background', 'red');
    } else if (colorSelect0 === "vert") {
        console.log(colorSelect0);
        $('#color0').css('background', 'green');
    } else if (colorSelect0 === "orange") {
        console.log(colorSelect0);
        $('#color0').css('background', 'orange');
    } else if (colorSelect0 === "bleu") {
        console.log(colorSelect0);
        $('#color0').css('background', 'blue');
    } else if (colorSelect0 === "marron") {
        console.log(colorSelect0);
        $('#color0').css('background', 'brown');
    } else if (colorSelect0 === "noir") {
        console.log(colorSelect0);
        $('#color0').css('background', 'black');
    }

    let colorSelect1 = $('#color1').val();
    if (colorSelect1 === "rouge") {
        console.log(colorSelect1);
        $('#color1').css('background', 'red');
    } else if (colorSelect1 === "vert") {
        console.log(colorSelect1);
        $('#color1').css('background', 'green');
    } else if (colorSelect1 === "orange") {
        console.log(colorSelect1);
        $('#color1').css('background', 'orange');
    } else if (colorSelect1 === "bleu") {
        console.log(colorSelect1);
        $('#color1').css('background', 'blue');
    } else if (colorSelect1 === "marron") {
        console.log(colorSelect1);
        $('#color1').css('background', 'brown');
    } else if (colorSelect1 === "noir") {
        console.log(colorSelect1);
        $('#color1').css('background', 'black');
    }

    let colorSelect2 = $('#color2').val();
    if (colorSelect2 === "rouge") {
        console.log(colorSelect2);
        $('#color2').css('background', 'red');
    } else if (colorSelect2 === "vert") {
        console.log(colorSelect2);
        $('#color2').css('background', 'green');
    } else if (colorSelect2 === "orange") {
        console.log(colorSelect2);
        $('#color2').css('background', 'orange');
    } else if (colorSelect2 === "bleu") {
        console.log(colorSelect2);
        $('#color2').css('background', 'blue');
    } else if (colorSelect2 === "marron") {
        console.log(colorSelect2);
        $('#color2').css('background', 'brown');
    } else if (colorSelect2 === "noir") {
        console.log(colorSelect2);
        $('#color2').css('background', 'black');
    }

    let colorSelect3 = $('#color3').val();
    if (colorSelect3 === "rouge") {
        console.log(colorSelect3);
        $('#color3').css('background', 'red');
    } else if (colorSelect3 === "vert") {
        console.log(colorSelect3);
        $('#color3').css('background', 'green');
    } else if (colorSelect3 === "orange") {
        console.log(colorSelect3);
        $('#color3').css('background', 'orange');
    } else if (colorSelect3 === "bleu") {
        console.log(colorSelect3);
        $('#color3').css('background', 'blue');
    } else if (colorSelect3 === "marron") {
        console.log(colorSelect3);
        $('#color3').css('background', 'brown');
    } else if (colorSelect3 === "noir") {
        console.log(colorSelect3);
        $('#color3').css('background', 'black');
    }

    let colorSelect4 = $('#color4').val();
    if (colorSelect4 === "rouge") {
        console.log(colorSelect4);
        $('#color4').css('background', 'red');
    } else if (colorSelect4 === "vert") {
        console.log(colorSelect4);
        $('#color4').css('background', 'green');
    } else if (colorSelect4 === "orange") {
        console.log(colorSelect4);
        $('#color4').css('background', 'orange');
    } else if (colorSelect4 === "bleu") {
        console.log(colorSelect4);
        $('#color4').css('background', 'blue');
    } else if (colorSelect4 === "marron") {
        console.log(colorSelect4);
        $('#color4').css('background', 'brown');
    } else if (colorSelect4 === "noir") {
        console.log(colorSelect4);
        $('#color4').css('background', 'black');
    }

}

$(document).ready(bgcolor);
$('#color0').change(bgcolor);
$('#color1').change(bgcolor);
$('#color2').change(bgcolor);
$('#color3').change(bgcolor);
$('#color4').change(bgcolor);