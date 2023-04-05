$(function() {
    $.ajax({
        url: 'https://bigquery.googleapis.com/bigquery/v2/projects/sanguine-orb-379207/queries',
        type: 'POST',
        contentType: 'application/json',
        headers: {
            'Authorization': 'AIzaSyArx2joqCHzACI9aDOis4-aSb8HApT4QAw'
        },
        data: JSON.stringify({
            query: 'SELECT nombre, id, clasificacion, precio, fecha_de_salida, stock FROM `sanguine-orb-379207.Juegos.Games` LIMIT 1000',
            useLegacySql: false
        }),
        success: function(response) {
            var rows = response['rows'];
            var table = $('#resultado');
            var header = $('<tr>').append(
                $('<th>').text('Nombre'),
                $('<th>').text('ID'),
                $('<th>').text('Clasificación'),
                $('<th>').text('Precio'),
                $('<th>').text('Fecha de salida'),
                $('<th>').text('Stock')
            );
            table.append(header);
            $.each(rows, function(index, row) {
                var cells = row['f'];
                var tableRow = $('<tr>').append(
                    $('<td>').text(cells[0]['v']),
                    $('<td>').text(cells[1]['v']),
                    $('<td>').text(cells[2]['v']),
                    $('<td>').text(cells[3]['v']),
                    $('<td>').text(moment(cells[4]['v']).format('YYYY-MM-DD')),
                    $('<td>').text(cells[5]['v'])
                );
                table.append(tableRow);
            });
        },
        error: function(error) {
            console.log(error);
        }
    });
});
