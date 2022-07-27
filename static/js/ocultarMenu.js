window.onload=cargar();
function cargar(){
    
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="hidden";
    document.getElementById("menues").style.position="absolute";
    document.getElementById("menues").style.position="relative";
    document.getElementById("frmExploracion").style.visibility="hidden";
    document.getElementById("menues").style.visibility="visible";
    document.getElementById("tituloDiagnosticoGenerado").style.visibility="hidden"; 
    document.getElementById("tituloDiagnosticoGenerado").style.position="absolute"; 

    /*----ABOSLUTO*/
    document.getElementById("frmConsulta").style.position="absolute";
    document.getElementById("frmDatos").style.position="absolute";
    document.getElementById("frmExploracion").style.position="absolute";
    document.getElementById("frmOdontograma").style.position="absolute";
    document.getElementById("menues").style.position="absolute";
    document.getElementById("menues").style.position="absolute";
    document.getElementById("menues").style.position="absolute";
    document.getElementById("menues").style.position="absolute";
}

/*-----FUNCIONES DEL MENÚ-----*/

function menuPaciente(){
    var id;
    id=document.getElementById("datosPaciente");
    if (id.click)

    document.getElementById("frmDatos").style.position="relative"; 
    document.getElementById("menues").style.position="absolute";
    document.getElementById("menues").style.visibility="hidden";
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="visible";
    document.getElementById("frmExploracion").style.visibility="hidden"; 
    document.getElementById("frmSignos").style.visibility="hidden";
    
}

function menuExploracion(){
    var id;
    id=document.getElementById("exploracionPaciente");
    if (id.click)
    document.getElementById("frmExploracion").style.position="relative";
    document.getElementById("menues").style.position="relative";
    document.getElementById("frmDatos").style.position="absolute";
    document.getElementById("frmConsulta").style.position="absolute";
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmDatos").style.visibility="hidden";
    document.getElementById("frmExploracion").style.visibility="visible"; 
    document.getElementById("menues").style.visibility="visible";  
}

function menuOdontograma(){
    var id;
    id=document.getElementById("odontogramaPaciente");
    if (id.click)
    document.getElementById("").show();
}

function menuDiagnostico(){
    var id;
    id=document.getElementById("diagnosticoPaciente");
    if (id.click)
    document.getElementById("").show();
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
    document.getElementById("frmConsulta").style.visibility="hidden";
    document.getElementById("frmExploracion").style.position="relative";
    document.getElementById("frmExploracion").style.visibility="visible";
}

function subSegundo(){
    var id;
    id=document.getElementById("enfermedad");
    if(id.click)
    document.getElementById("frmConsulta").style.position="relative";
    document.getElementById("frmExploracion").style.visibility="hidden";
    document.getElementById("frmExploracion").style.position="absolute";
    document.getElementById("frmConsulta").style.visibility="visible";
    
}

// function ocultar(){
//     print()
//     document.getElementById("frmDatos").style.visibility="visible";
//     document.getElementById("frmConsulta").style.visibility="hidden";
//     document.getElementById("frmExploracion").style.visibility="hidden";
// }