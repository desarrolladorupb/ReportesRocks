$(document).ready(function(){

	var cmbComites ;
	var txtFechaInicio=$("#txtFechaInicio");
	var txtFechaFin=$("#txtFechaFin");

	var tblStatus=$("#tblStatus").DataTable({
        dom: 'Bfrtip',
        buttons: [
             'excel', 'pdf'
        ]
    });
	var tblSeguimiento=$("#tblSeguimiento").DataTable({
        dom: 'Bfrtip',
        buttons: [
             'excel', 'pdf'
        ]
    });
	var tblEpMeeting=$("#tblEpMeeting").DataTable({
        dom: 'Bfrtip',
        buttons: [
             'excel', 'pdf'
        ]
    });
	var tblApprovedUniversidad=$("#tblApprovedUniversidad").DataTable({
        dom: 'Bfrtip',
        buttons: [
             'excel', 'pdf'
        ]
    });
	var tblTasaConversion=$("#tblTasaConversion").DataTable({
        dom: 'Bfrtip',
        buttons: [
             'excel', 'pdf'
        ]
    });
	var Cargando='<div class="preloader-wrapper active">'+
				    '<div class="spinner-layer spinner-red-only">'+
				     '<div class="circle-clipper left">'+
				        '<div class="circle"></div>'+
				      '</div><div class="gap-patch">'+
				        '<div class="circle"></div>'+
				      '</div><div class="circle-clipper right">'+
				        '<div class="circle"></div>'+
				      '</div>'+
				    '</div>'+
				  '</div>';

	var ConsultarComites=function(){
		$.ajax({
		    url: '/reportes_ogv/comites',
		    type: "GET",
		    data: {},
		    beforeSend:function(objeto){
		    	swal({   title: "<small>Cargando datos ...</small>"
		    		,   text: Cargando
		    		,   html: true 
		    		,  showCancelButton: false
					, showConfirmButton: false
						});
		    },
		    success: function (response) {
		    
		    	$.each(response,function(index,value){
		    		var options="<option value='"+value.ValorPodio+"'>"+value.Comite+"</option>"
		    		$("#cmbComites").append(options);

		    	});
		    	cmbComites =$("#cmbComites").select2();
		    	swal.close();       
		    }
		});
	}

	var PintarDatos=function(Comite){
		$.ajax({
		    url: '/reportes_ogv/data',
		    type: "GET",
		    data: {"Comite":Comite
		    		,"FechaInicio":txtFechaInicio.val()
		    		,"FechaFin":txtFechaFin.val()
			},
		    beforeSend:function(objeto){
		    	swal({   title: "<small>Cargando datos ...</small>"
		    		,   text: Cargando
		    		,   html: true 
		    		,  showCancelButton: false
					, showConfirmButton: false
						});
		    },
		    success: function (response) {		    	
		    	tblStatus.clear().draw();
				tblSeguimiento.clear().draw();
				tblEpMeeting.clear().draw();
				tblApprovedUniversidad.clear().draw();
				tblTasaConversion.clear().draw();

		    	PintarStatus(response.lstStatus);
		    	PintarSeguimiento(response.lstSegumiento);
		    	PintarEpMeeting(response.lstEpMeeting);
		    	PintarUniversityApproved(response.lstUniversity);
		    	PintarTasaConversion(response.lstConversion);
		    	swal("Terminado", "Datos Cargados correctamente", "success");
		       
		    }
		});
	};

	var PintarStatus=function(lstStatus){
		var ArrayData=[["Status","Valor"]];
		var NumeroRegistros=0;
		$.each(lstStatus,function(index,value){
			ArrayData.push([index,value]);
			NumeroRegistros+=value;
		});
		
		var data = google.visualization.arrayToDataTable(
          ArrayData
        );
        var options = {
          title: 'Status'
          ,width:900
         ,height:500
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechartStatus'));
        chart.draw(data, options);
        $.each(lstStatus,function(index,value){
        	var Procentaje=(value*100)/NumeroRegistros;
        	tblStatus
			    .row.add( [ index, value, Procentaje.toFixed(2)+"%" ] )
			    .draw()

        });


	};

	var PintarSeguimiento=function(lstSeguimiento){
		var ArrayData=[["Seguimiento","Valor"]];
		var NumeroRegistros=0;
		$.each(lstSeguimiento,function(index,value){
			ArrayData.push([index,value]);
			NumeroRegistros+=value;
		});
		var data = google.visualization.arrayToDataTable(
          ArrayData
        );
        var options = {
          title: 'Seguimiento'
          ,width:900
         ,height:500
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechartSeguimiento'));
        chart.draw(data, options);
        $.each(lstSeguimiento,function(index,value){
        	var Procentaje=(value*100)/NumeroRegistros;
        	tblSeguimiento
			    .row.add( [ index, value, Procentaje.toFixed(2)+"%" ] )
			    .draw()

        });
		
	};

	var PintarEpMeeting=function(lstEpMeeting){
		var ArrayData=[["EP Meeting","Valor"]];
		var NumeroRegistros=0;
		$.each(lstEpMeeting,function(index,value){
			ArrayData.push([index,value]);
			NumeroRegistros+=value;
		});
		var data = google.visualization.arrayToDataTable(
          ArrayData
        );
        var options = {
          title: 'Seguimiento'
          ,width:900
         ,height:500
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechartEpMeeting'));
        chart.draw(data, options);
        $.each(lstEpMeeting,function(index,value){
        	var Procentaje=(value*100)/NumeroRegistros;
        	tblEpMeeting
			    .row.add( [ index, value, Procentaje.toFixed(2)+"%" ] )
			    .draw()

        });
	};

	var PintarUniversityApproved=function(lstUniversityApproved){
		var ArrayData=[["Universidad","Valor"]];
		var NumeroRegistros=0;
		$.each(lstUniversityApproved,function(index,value){
			ArrayData.push([index,value]);
			NumeroRegistros+=value;
		});
		var data = google.visualization.arrayToDataTable(
          ArrayData
        );
        var options = {
          title: 'Approved X Universidad'
          ,width:900
         ,height:500
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechartApproved'));
        chart.draw(data, options);
        $.each(lstUniversityApproved,function(index,value){
        	var Procentaje=(value*100)/NumeroRegistros;
        	tblApprovedUniversidad
			    .row.add( [ index, value, Procentaje.toFixed(2)+"%" ] )
			    .draw()

        });
	};

	var PintarTasaConversion=function(lstTasaConversion){
		var ArrayData=[["Open","Approved"]];
		var TasaConversion=0;
		ArrayData.push(["Open",(lstTasaConversion.Open-lstTasaConversion.Approved)]);
		ArrayData.push(["Approved",lstTasaConversion.Approved]);
		

		TasaConversion=Math.round((lstTasaConversion.Open/lstTasaConversion.Approved));
		var data = google.visualization.arrayToDataTable(
          ArrayData
        );
        var options = {
          title: 'Aplicantes - '+lstTasaConversion.Open
          ,width:900
         ,height:500
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechartTasaConversion'));
        chart.draw(data, options);        
        	
    	tblTasaConversion
		    .row.add( ["Aplicantes",lstTasaConversion.Open])
		    .draw();
		tblTasaConversion
		    .row.add( ["Open",(lstTasaConversion.Open-lstTasaConversion.Approved)])
		    .draw();
		tblTasaConversion
		    .row.add(["Approved",lstTasaConversion.Approved])
		    .draw();

		tblTasaConversion
		    .row.add(["Tasa de Conversion","1 a "+TasaConversion])
		    .draw();

        
	};

	$("#cmbComites").on("change",function(){
		
		PintarDatos(cmbComites.val())
	});
	$('.datepicker').pickadate({
    	selectMonths: true, // Creates a dropdown to control month
   		selectYears: 15,
   		format: 'yyyy-mm-dd' ,
  	});
       
	$("#menuOGV").addClass("active");
	google.charts.load('current', {'packages':['corechart']});
	google.charts.setOnLoadCallback(ConsultarComites);
});
