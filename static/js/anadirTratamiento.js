    var saldo=0
    var color=""

    function obtenerSaldo(b){
        saldo = $('option:selected', b).attr('valor');
    }

    function cargarFigura(){
        let identificadores=["TP18","BP18","RP18","LP18","CP18","CP17","TP17","BP17","RP17","LP17","CP16",
        "TP16","BP16","RP16","LP16","CP15","TP15","BP15","RP15","LP15","CP14","TP14","BP14","RP14","LP14",
        "CP13","TP13","BP13","RP13","LP13","CP12","TP12","BP12","RP12","LP12","CP11","TP11","BP11","RP11",
        "LP11","CP55","TP55","BP55","RP55","LP55","CP54","TP54","BP54","RP54","LP54","CP53","TP53","BP53",
        "RP53","LP53","CP52","TP52","BP52","RP52","LP52","CP51","TP51","BP51","RP51","LP51","CP85","TP85",
        "BP85","RP85","LP85","CP84","TP84","BP84","RP84","LP84","CP83","TP83","BP83","RP83","LP83","CP82",
        "TP82","BP82","RP82","LP82","CP81","TP81","BP81","RP81","LP81","CP48","TP48","BP48","RP48","LP48",
        "CP47","TP47","BP47","RP47","LP47","CP46","TP46","BP46","RP46","LP46","CP45","TP45","BP45","RP45",
        "LP45","CP44","TP44","BP44","RP44","LP44","CP43","TP43","BP43","RP43","LP43","CP42","TP42","BP42",
        "RP42","LP42","CP41","TP41","BP41","RP41","LP41","CP21","TP21","BP21","RP21","LP21","CP22","TP22",
        "BP22","RP22","LP22","CP23","TP23","BP23","RP23","LP23","CP24","TP24","BP24","RP24","LP24","CP25",
        "TP25","BP25","RP25","LP25","CP26","TP26","BP26","RP26","LP26","CP27","TP27","BP27","RP27","LP27",
        "CP28","TP28","BP28","RP28","LP28","CP61","TP61","BP61","RP61","LP61","CP62","TP62","BP62","RP62",
        "LP62","CP63","TP63","BP63","RP63","LP63","CP64","TP64","BP64","RP64","LP64","CP65","TP65","BP65",
        "RP65","LP65","CP71","TP71","BP71","RP71","LP71","CP72","TP72","BP72","RP72","LP72","CP73","TP73",
        "BP73","RP73","LP73","CP74","TP74","BP74","RP74","LP74","CP75","TP75","BP75","RP75","LP75","CP31",
        "TP31","BP31","RP31","LP31","CP32","TP32","BP32","RP32","LP32","CP33","TP33","BP33","RP33","LP33",
        "CP34","TP34","BP34","RP34","LP34","CP35","TP35","BP35","RP35","LP35","CP36","TP36","BP36","RP36",
        "LP36","CP37","TP37","BP37","RP37","LP37","CP38","TP38","BP38","RP38","LP38"]
        for (var i = 0; i < identificadores.length; i++) {
            color=document.getElementById(identificadores[i]).style.fill;
            if (color == ''){
                color="white"
            }
            $('#tbIdentificador tbody').append($('<tr>', {}).append(
                $('<td>', {}).append($('<input>', {
                    'class': 'txtOpcion',
                    'type': 'text',
                    'readonly':'any',
                    'style': 'height:6vh;border-radius:4px;padding-left:20px',
                    'name': 'identificador[]',
                    'value':identificadores[i]
                })),
                $('<td>', {}).append($('<input>', {
                    'class': 'txtOpcion',
                    'type': 'text',
                    'readonly':'any',
                    'style': 'height:6vh;border-radius:4px;padding-left:20px',
                    'required': 'true',
                    'name': 'color[]',
                    'value':color
                })),
                $('<td>').append($('<button>', {
                    'type': 'button',
                    'class': 'btn btn-danger btn-sm agregar',
                    'html': '<i class="fa fa-trash">Descartar</i>',
                    'style': 'background:red;color:white;border-radius:4px;border-color:red;'
                }))
                
            ));
        }
        
        
        
    }

    function sobrePintar(){
        var resume_table = document.getElementById("tbIdentificador");

        for (var i = 0, row; row = resume_table.rows[i]; i++) {
        //alert(cell[i].innerText);
            for (var j = 0, col; col = row.cells[j]; j++) {
                //alert(col[j].innerText);
                alert(`Txt: ${col.innerText} \tFila: ${i.value} \t Celda: ${j}`);
            }
        }
        

    }

    $('#btnAdd').click(function () {
        var verificar=document.getElementById("listaTratamiento"); 
        var conclusion=document.getElementById("tratamiento__Conclusion")
        var final=verificar.options[verificar.selectedIndex].text;
        var finalConclusion=conclusion.value;
        var valor=document.getElementById('listaTratamiento').value;
        var valorActual=document.getElementById('txtSaldo').value;
        if (valorActual==''){
            document.getElementById('txtSaldo').value=0
        }
        if (valor != 'Seleccione Tratamiento'){
            document.getElementById('txtSaldo').value=Number(valorActual)+Number(saldo)
        }
        
        /*var saldo=saldoLista.options[saldoLista.selectedIndex].data().text;*/


        if (valor != 'Seleccione Tratamiento'){
            $('#tbDetalle tbody').append($('<tr>', {}).append(
                $('<td>', {}).append($('<input>', {
                    'class': 'txtOpcion',
                    'type': 'text',
                    'readonly':'any',
                    'style': 'height:6vh;border-radius:4px;padding-left:20px',
                    'name': 'rucsap[]',
                    'value':final
                })),
                $('<td>', {}).append($('<input>', {
                    'class': 'contenedorPac__Principal__Uno__ingreso',
                    'type': 'text',
                    'readonly':'any',
                    'required': 'true',
                    'hidden':'any',
                    'name': 'idTratamientoSelect[]',
                    'value':valor
                })),
                $('<td>', {}).append($('<input>', {
                    'class': 'contenedorPac__Principal__Uno__ingreso',
                    'type': 'text',
                    'readonly':'any',
                    'required': 'true',
                    'hidden':'any',
                    'name': 'txtConclusion[]',
                    'value':finalConclusion
                })),
                $('<td>', {}).append($('<input>', {
                    'class': 'txtOpcion',
                    'type': 'text',
                    'readonly':'any',
                    'style': 'height:6vh;border-radius:4px;padding-left:20px',
                    'name': 'saldo[]',
                    'id':'valor',
                    'value':saldo
                })),
                $('<td>').append($('<button>', {
                    'type': 'button',
                    'class': 'btn btn-danger btn-sm deleteFila',
                    'html': '<i class="fa fa-trash">Descartar</i>',
                    'style': 'background:red;color:white;border-radius:4px;border-color:red;'
                }))
            ));
        }
        
    });

    $('#tbDetalle').on('click', 'tbody tr td .deleteFila', function () {
        $(this).parents('tr').remove();
        var valores= new Array();
        i=0;

 

        $(this).parents("tr").find("td").each(function(){
            valores[i] =$(this).html();
            i++;
        });
        var variable=valores[3]
        var tamano=variable.length
        var tamanoReducido=Number(tamano)-2
        var cadena=variable.substring(145, tamanoReducido)
        var valorAumentado=document.getElementById('txtSaldo').value;
        var disminuir=Number(valorAumentado)-Number(cadena);
        document.getElementById('txtSaldo').value=disminuir;        
    })

    