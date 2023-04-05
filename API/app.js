$(document).ready(function() {
    setInterval(function() {
      $.ajax({
        url: "/get_data",
        type: "get",
        success: function(response) {
          $("#data").html(response);
        },
        error: function(xhr) {
          console.log(xhr);
        }
      });
    }, 5000); // Actualizar cada 5 segundos (5000 milisegundos)
  });
  