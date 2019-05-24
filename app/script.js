$( function() {
    $( "#tabs" ).tabs();
    $( "#tabs2" ).tabs();

    $("#btn_prueba").click(function()
    {
      alert("aaaaaaaaaaaaaaaaaaaa");
    });

    
  }
);


/*$(document).ready(function() {

  $(".js-boton").mousedown(function(event) {
    event.preventDefault(); // Esto no es necesario, es por vicio xD
    var comando = $(this).attr('data-type');
    document.execCommand(comando, false, null);
  });

  $('#js-enlaces').mousedown(function(event) {
    var cadena;
    saveSelection();
    cadena = "<div id='js-bodyDialog'>";
    cadena += "<input type='text' id='js-inputURL' /><br />";
    cadena += "<button id='js-aceptar'>Aceptar</button>";
    cadena += "<button id='js-cancelar'>Cancelar</button>";
    cadena += "</div>";
    $('#js-dialog').html(cadena).show();

    $('#js-cancelar').click(function() {
      $('#js-bodyDialog').remove();
      $('#js-dialog').hide();
    });


    $('#js-aceptar').click(function(event) {
      event.preventDefault();
      var href = $('#js-inputURL').val().trim().toLowerCase();
      restoreSelection();
      document.execCommand("createLink", false, href);
      $('#js-bodyDialog').remove();
      $('#js-dialog').hide();
    });

  });

  var selectedRange;

  function getCurrentRange() {
    var sel = window.getSelection();
    if (sel.getRangeAt && sel.rangeCount) {
      return sel.getRangeAt(0);
    }
  }

  function saveSelection() {
    selectedRange = getCurrentRange();
  }

  function restoreSelection() {
    var selection = window.getSelection();
    if (selectedRange) {
      try {
        selection.removeAllRanges();
      } catch (ex) {
        document.body.createTextRange().select();
        document.selection.empty();
      }

      selection.addRange(selectedRange);
    }
  }

});
*/
