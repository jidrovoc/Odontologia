var idFuncion;
var color=0;
var verificaColor=0;
var cuenta=0;
function obtenerOpcion(b){
    idFuncion=b.id;
    color=1;

}


function obtenerIdPoligono( b ){ 
var id=b.id
var color=b.style.fill;

if (cuenta == 0){
    if (color = 1){
        cuenta = cuenta + 1;
        /*$('<input/>').attr({type:'text',value:'2',name:"odontoVerificador"+i}).appendTo('#opcionesOdontograma');*/
        document.getElementById("odontoloVerificador").value =2;
        
    }
}


switch(idFuncion){
    case "opcionObservacion":
    document.getElementById(id).style.fill="rgb(103, 182, 103)"
    break;
    
    case "opcionAusente":
    document.getElementById(id).style.fill="rgb(76, 77, 80)"
    break;

    case "opcionRadicular":
    document.getElementById(id).style.fill="rgb(47, 36, 199)"
    break;

    case "opcionCarie":
    document.getElementById(id).style.fill="rgb(112, 175, 194)"
    break;

    case "opcionCorona":
    document.getElementById(id).style.fill="rgb(48, 47, 146)"
    break;

    case "opcionIncrustacion":
    document.getElementById(id).style.fill="rgb(176, 201, 176)"
    break;

    case "opcionClavija":
    document.getElementById(id).style.fill="rgb(8, 112, 8)"
    break;

    case "opcionFractura":
    document.getElementById(id).style.fill="rgb(204, 180, 143)"
    break;

    case "opcionEndodoncia":
    document.getElementById(id).style.fill="rgb(208, 150, 241)"
    break;

    case "opcionObturacion":
    document.getElementById(id).style.fill="rgb(140, 67, 158)"
    break;

    case "opcionIntrusion":
    document.getElementById(id).style.fill="rgb(216, 95, 210)"
    break;

    case "opcionExtrusion":
    document.getElementById(id).style.fill="rgb(233, 213, 102)"
    break;

    case "opcionProtesis":
    document.getElementById(id).style.fill="rgb(230, 77, 77)"
    break;

    case "opcionImplante":
    document.getElementById(id).style.fill="rgb(83, 53, 28)"
    break;

    case "opcionOrtodoncia":
    document.getElementById(id).style.fill="rgb(221, 224, 48)"
    break;

    case "opcionEdentulo":
    document.getElementById(id).style.fill="rgb(0, 0, 0)"
    break;
}

}

