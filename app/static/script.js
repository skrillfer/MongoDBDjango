  $( function() {

      $(".lined").linedtextarea(
		    {selectedLine: 1}
	     );
       var RUTA="";
       var contador=2;
       var ultimoTag="#tabs-SQL";

       //_______________________________________________________________________
       //$('#tabs-4').hide();
       $('#li2').hide();
       $('#li3').hide();
       $('#li4').hide();
       $('#li5').hide();
       $('#li6').hide();
       $('#li7').hide();
       $('#li8').hide();
       $('#li9').hide();
       $('#li10').hide();
       $('#li11').hide();
       $('#li12').hide();
       $('#li13').hide();
       $('#li14').hide();
       $('#li15').hide();

       $('#tabs-2').hide();
      $('#tabs-3').hide();
      $('#tabs-4').hide();
      $('#tabs-5').hide();
      $('#tabs-6').hide();
      $('#tabs-7').hide();
      $('#tabs-8').hide();
      $('#tabs-9').hide();
      $('#tabs-10').hide();
      $('#tabs-11').hide();
      $('#tabs-12').hide();
      $('#tabs-13').hide();
      $('#tabs-14').hide();
      $('#tabs-15').hide();




      $( "#tabs" ).tabs();
      $( "#tabs2" ).tabs();

      // cuando se selecciona un LI
      $("#ul1 li").click(function() {
           //alert(this.href);
           ultimoTag = $("a",this).attr('href');
           //alert(ultimoTag);
           //alert($("a",this).attr('id'));
           /*var div1=$(ultimoTag).attr('id');


           div1=ultimoTag+"-text";
           alert(div1);

           if ($.trim($(div1).val()) != "") {
              alert($("#tabs-SQL-text").val());
           }*/
       });

       //--------------------Acciones de los botones----------------------------
         $("#btn_guardar").click(function() {
             var div1=ultimoTag+"-text";
             //alert(div1);
             if ($.trim($(div1).val()) != "") {
                alert($(div1).val());
             }
         });
         //--------------------------------------------------------------------
         $("#btn_ejecutar").click(function() {
           var div1=ultimoTag+"-text";

           if ($.trim($(div1).val()) != "") {
              var Ipaq ="usql";//tipo de paquete
              var Inst =$(div1).val();//instruccion SQL
              Inst=Inst.replace(/\"/g , "\'");

              var Ius  =$("#usuario000").attr('href');    Ius=Ius.replace("#","");// usuario actual

              $.ajax({type: 'POST',
                   url: "/home/"+usuario000+"/",                            // some data url
                   data: {paquete: Ipaq, instruccion: Inst, usuario:Ius},       // some params
                   success: function (response) {                  // callback
                     alert(response.result);
                   }
              });
           }
         });
         //--------------------------------------------------------------------
         $("#btn_abrir").click(function() {
              document.getElementById('my_file').click();
         });

         //----- es un hanldre que se activa cuando input file cambia-----------
         $('input[type=file]').change(function (e) {
            tmppp=$(this).files[0].mozFullPath;
            alert(tmppp);
            RUTA=$(this).val();

            if(RUTA!=""){
                alert(RUTA);

            }
              //$('#customfileupload').html($(this).val());
        });

         $("#btn_ejecutar").click(function() {
           alert("pendejos1");
           var url = "";
           alert("pendejos2");
           var pieFact = "hola mundo";
           var data = {'pieFact': pieFact};

           var link = document.getElementById("usuario000");

           var usuario000=$("#usuario000").attr('href');
           usuario000=usuario000.replace("#","");
           $.ajax({type: 'POST',
                url: "/home/"+usuario000+"/",                            // some data url
                data: {param: 'hello', another_param: 5},       // some params
                success: function (response) {                  // callback
                  alert(response.result);
                    /*if (response.result === 'OK') {
                        if (response.data && typeof(response.data) === 'object') {
                          alert("todo bien");
                            // do something with the successful response.data
                            // e.g. response.data can be a JSON object
                        }
                    } else {
                        // handle an unsuccessful response
                    }*/
                }
           });

         });
       //--------------------QUITAR TAB-----------------------------------------
       $("#btn_quitTab").click(function() {
          if(contador>2){
            contador=contador-1;
            var idLi="#li"+contador;
            var ref = $("a",idLi).attr('href');
            $(ref+"-text").val("");
            $(idLi).hide();
          }

       });
       //--------------------AGREGAR TAB ---------------------------------------
      $("#btn_addTab").click(function()
      {
        var idLi="#li"+contador;

        $(idLi).show();
          //$('#li4').show();
        contador=contador+1;
        /*
       var list = document.getElementsByClassName("col-sm-8 text-left");
       var colum1 = list[0];
       var hijos = colum1.children;
       //_______________________________________________________________________
       var tabs = hijos[0];
       var ul1=tabs.children[0];

       var copia =  ul1.children[ul1.children.length - 1];
       var Ultimo = copia.cloneNode(true);


       var litmp = ul1.children[ul1.children.length - 2];

       var li_n = litmp.cloneNode(true);//document.createElement('li');
       var nmTab = new Date().toLocaleTimeString('en-US', { hour12: false,hour: "numeric",minute: "numeric",second: "numeric"});
       nmTab=nmTab.replace(":", "_");
       nmTab=nmTab.replace(":", "_");

       li_n.innerHTML =litmp.innerHTML; //"<a href=\"#tabs-"+nmTab+"\">"+nmTab+"</a>";
       var h_1= li_n.children[0];
       h_1.href="#tabs-"+nmTab;

       var Div1Tmp = tabs.children[tabs.children.length - 2];
       //var div_n = Div1Tmp.cloneNode(true);
       //div_n.id='tabs-'+nmTab;
       var div_n = Div1Tmp.cloneNode(true);
       div_n.id='tabs-'+nmTab;
       div_n.text='tabs-'+nmTab;
       div_n.innerHTML = Div1Tmp.innerHTML;

       ul1.removeChild(ul1.children[ul1.children.length - 1]);
       ul1.removeChild(ul1.children[ul1.children.length - 1]);


       tabs.appendChild(div_n);
       ul1.appendChild(li_n);


       //_________________________agregando el nuevo DIV a TABS_________________
       /*var div_n = document.createElement('div');
       div_n.id='tabs-'+nmTab;
       div_n.innerHTML ='  <div class="form-group">'+
                        '     <textarea class="form-control" rows="10" id="comment"></textarea>'+
                        '  </div>';
       tabs.appendChild(div_n);
*/
      //ul1.appendChild(Ultimo);
       //alert(tabs.children.length);

      });

    }
  );
