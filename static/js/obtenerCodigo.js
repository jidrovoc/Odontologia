window.onload=cargarSelect(),cargarSelectCita();

function obtenerPaciente(b){
    document.getElementById("idPaciente").value=b.value
}

function obtenerDoctor(b){
    document.getElementById("idDoctor").value=b.value
}

function obtenerArea(b){
    document.getElementById("idArea").value=b.value
}

function cargarSelect(){
    if (document.getElementById("idArea")) {
        var id=document.getElementById("idArea").value;
        document.getElementById("selectArea").value=id;
    }   
}

function cargarSelectCita(){
    if(document.getElementById("idDoctor")){
        var idPa=document.getElementById("idPaciente").value;
        document.getElementById("listaPaciente").value=idPa;
        var idDo=document.getElementById("idDoctor").value;
        document.getElementById("listaDoctor").value=idDo;
        
        var fecha=document.getElementById("fechaValor").value;

        
        // document.getElementById("editarFecha").value=fecha;
        var mes = fecha.getMonth()+1; //obteniendo mes
        var dia = fecha.getDate(); //obteniendo dia
        var ano = fecha.getFullYear(); //obteniendo año
        if(dia<10)
            dia='0'+dia; //agrega cero si el menor de 10
        if(mes<10)
            mes='0'+mes //agrega cero si el menor de 10
        document.getElementById('editarFecha').value=fecha;
    }
}

