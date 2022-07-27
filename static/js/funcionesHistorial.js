window.onload=cargar();

/*----------VARIABLES GLOBALES----------*/
var idFuncion;

function cargar(){
    document.getElementById("historyOdontograma").style.visibility="hidden";
    document.getElementById("historyOdontograma").style.position="absolute";
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="visible";
    document.getElementById("menues").style.position="absolute";

    document.getElementById("frmAlergia").style.visibility="hidden";
    document.getElementById("frmAlergia").style.position="absolute";

    document.getElementById("frmExploracion").style.visibility="hidden";
    document.getElementById("menues").style.visibility="hidden"; 
    document.getElementById("frmSignos").style.visibility="hidden"; 
    document.getElementById("interdazDiagnostico").style.visibility="hidden";
    document.getElementById("interdazDiagnostico").style.position="absolute";
    document.getElementById("interfazTratamientoRealizado").style.visibility="hidden";
    document.getElementById("interfazTratamientoRealizado").style.position="absolute";

    document.getElementById("tituloDiagnosticoGenerado").style.visibility="hidden"; 
    document.getElementById("tituloDiagnosticoGenerado").style.position="absolute"; 

    /*----ABOSLUTO*/
    
    document.getElementById("frmConsulta").style.position="absolute";
    document.getElementById("frmDatos").style.position="relative";
    document.getElementById("frmExploracion").style.position="absolute";


}

/*-----FUNCIONES DEL MENÚ-----*/

function menuPaciente(){
    var id;
    id=document.getElementById("datosPaciente");
    if (id.click)
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmAlergia").style.visibility="hidden"
    document.getElementById("frmAlergia").style.position="absolute"
    document.getElementById("frmDatos").style.position="relative"; 
    document.getElementById("menues").style.position="absolute";
    document.getElementById("menues").style.visibility="hidden";
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="visible";
    document.getElementById("frmExploracion").style.visibility="hidden"; 
    document.getElementById("frmSignos").style.visibility="hidden";
    document.getElementById("frmSignos").style.position="absolute";
    
}

function menuExploracion(){
    var id;
    id=document.getElementById("exploracionPaciente");
    if (id.click)
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmAlergia").style.visibility="hidden"
    document.getElementById("frmAlergia").style.position="absolute"
    document.getElementById("frmExploracion").style.position="relative";
    document.getElementById("menues").style.position="relative";
    document.getElementById("frmDatos").style.position="absolute";
    document.getElementById("frmConsulta").style.position="absolute";
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="hidden";
    document.getElementById("frmExploracion").style.visibility="visible"; 
    document.getElementById("menues").style.visibility="visible"; 
    document.getElementById("frmSignos").style.visibility="hidden";
    document.getElementById("frmSignos").style.position="absolute"; 
}

function menuOdontograma(){
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="hidden";
    document.getElementById("menues").style.position="absolute";

    document.getElementById("frmAlergia").style.visibility="hidden";
    document.getElementById("frmAlergia").style.position="absolute";

    document.getElementById("frmExploracion").style.visibility="hidden";
    document.getElementById("menues").style.visibility="hidden"; 
    document.getElementById("frmSignos").style.visibility="hidden"; 

    /*----ABOSLUTO*/
    
    document.getElementById("frmConsulta").style.position="absolute";
    document.getElementById("frmDatos").style.position="absolute";
    document.getElementById("frmExploracion").style.position="absolute";

    document.getElementById("interfazOdontograma").style.visibility="visible";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("interfazOdontograma").style.top="14%"
    document.getElementById("svgselect").style.marginTop="50px"
}

function menuDiagnostico(){
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="hidden";
    document.getElementById("menues").style.position="absolute";

    document.getElementById("frmAlergia").style.visibility="hidden";
    document.getElementById("frmAlergia").style.position="absolute";

    document.getElementById("frmExploracion").style.visibility="hidden";
    document.getElementById("menues").style.visibility="hidden"; 
    document.getElementById("frmSignos").style.visibility="hidden"; 

    /*----ABOSLUTO*/
    
    document.getElementById("frmConsulta").style.position="absolute";
    document.getElementById("frmDatos").style.position="absolute";
    document.getElementById("frmExploracion").style.position="absolute";

    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("interdazDiagnostico").style.visibility="visible";
    document.getElementById("interdazDiagnostico").style.position="relative";
    document.getElementById("interdazDiagnostico").style.bottom="65%"
    document.getElementById("interdazDiagnostico").style.marginTop="50px"
    document.getElementById("tituloDiagnosticoGenerado").style.position="relative";
    document.getElementById("tituloDiagnosticoGenerado").style.bottom="85%"

}

function menuEvolucion(){
    var id;
    id=document.getElementById("evolucionPaciente");
    if (id.click)
    document.getElementById("").show();
    
}

function menuTratamiento(){
    var id;
    id=document.getElementById("tratamientoPaciente");
    if (id.click)
    document.getElementById("").show();
}




/*-----FUNCIONES DEL SUBMENÚ-----*/

function subEnfermedad(){
    var id;
    id=document.getElementById("signo");
    if(id.click)
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmAlergia").style.visibility="hidden"
    document.getElementById("frmAlergia").style.position="absolute"
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmConsulta").style.position="absolute";
    document.getElementById("frmExploracion").style.position="relative";
    document.getElementById("frmExploracion").style.visibility="visible";
    document.getElementById("frmDatos").style.visibility="hidden";
    document.getElementById("frmDatos").style.position="absolute";
    document.getElementById("frmSignos").style.visibility="hidden";
    document.getElementById("frmSignos").style.position="absolute";
}

function subSegundo(){
    var id;
    id=document.getElementById("enfermedad");
    if(id.click)
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmAlergia").style.visibility="hidden"
    document.getElementById("frmAlergia").style.position="absolute"
    document.getElementById("frmConsulta").style.position="relative";
    document.getElementById("frmExploracion").style.visibility="hidden";
    document.getElementById("frmExploracion").style.position="absolute";
    document.getElementById("frmConsulta").style.visibility="visible";
    document.getElementById("frmSignos").style.visibility="hidden";
    document.getElementById("frmSignos").style.position="absolute";
    
}

function subFisica(){
    var id;
    id=document.getElementById("exploracion");
    if(id.click)
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    document.getElementById("frmExploracion").style.visibility="hidden"
    document.getElementById("frmExploracion").style.position="absolute"
    
    document.getElementById("frmDatos").style.visibility="hidden"
    document.getElementById("frmDatos").style.position="absolute"

    document.getElementById("frmConsulta").style.visibility="hidden"
    document.getElementById("frmConsulta").style.position="absolute"

    document.getElementById("menues").style.visibility="visible"
    document.getElementById("menues").style.position="relative"

    document.getElementById("frmAlergia").style.visibility="hidden"
    document.getElementById("frmAlergia").style.position="absolute"


    document.getElementById("frmSignos").style.position="relative"
    document.getElementById("frmSignos").style.visibility="visible"
    document.getElementById("frmSignos").style.bottom="76%"
    document.getElementById("penultimoContenedor").style.position="absolute"
    document.getElementById("ultimoContenedor").style.position="relative"
    document.getElementById("penultimoContenedor").style.top="100%"
    document.getElementById("ultimoContenedor").style.marginBottom="100px";    
}

function subAlergia(){
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmExploracion").style.visibility="hidden"
    document.getElementById("frmExploracion").style.position="absolute"

    document.getElementById("frmPopUpAlergia").style.visibility="hidden";
    document.getElementById("frmPopUpAlergia").style.position="absolute";
    
    document.getElementById("frmDatos").style.visibility="hidden"
    document.getElementById("frmDatos").style.position="absolute"

    document.getElementById("frmConsulta").style.visibility="hidden"
    document.getElementById("frmConsulta").style.position="absolute"

    document.getElementById("frmSignos").style.visibility="hidden"
    document.getElementById("frmSignos").style.position="absolute"

    document.getElementById("menues").style.visibility="visible"
    document.getElementById("menues").style.position="relative"

    document.getElementById("frmAlergia").style.position="relative"
    document.getElementById("frmAlergia").style.visibility="visible"
    document.getElementById("frmAlergia").style.bottom="77%"
    document.getElementById("frmAlergia").style.marginLeft="9px"

 
    
}

function registrarAlergia(){ 
    subAlergia();
    
    document.getElementById("interfazOdontograma").style.visibility="hidden";
    document.getElementById("interfazOdontograma").style.position="absolute";
    document.getElementById("frmPopUpAlergia").style.position="relative";
    document.getElementById("frmPopUpAlergia").style.visibility="visible";
    
    document.getElementById("frmPopUpAlergia").style.bottom="172vh"
    document.getElementById("frmPopUpAlergia").style.right="10%"
    document.getElementById("frmRegistroAlergia").style.position="relative";
    document.getElementById("guardarAlergia").style.position="relative";
    document.getElementById("guardarAlergia").style.left="15%"
    document.getElementById("cancelarAlergia").style.position="relative";
    document.getElementById("cancelarAlergia").style.left="23.5%"
    document.getElementById("frmRegistroAlergia").style.boxShadow="2px 2px 5px #999"
    $(document).ajaxStart($.blockUI);
}


// function ocultar(){
//     print()
//     document.getElementById("frmDatos").style.visibility="visible";
//     document.getElementById("frmConsulta").style.visibility="hidden";
//     document.getElementById("frmExploracion").style.visibility="hidden";
// }


/*-----OBTENER ID-----*/
// function obtenerId(){
// // document.querySelectorAll(".figura").forEach(el => {
// //     el.addEventListener("click", e => {
// //         const id = e.target.getAttribute("id");
// //         print()
// //         console.log("Se ha clickeado el id "+id);
// //     });
// //     });
// const id = e.target.getAttribute("id");
// alert(id)
// }

function obtenerOpcion(b){
    idFuncion=b.id;
}

function obtenerIdPoligono( b ){
var id=b.id
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