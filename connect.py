import os 
from google.cloud import bigquery
from jinja2 import Template

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'clouddemo-service-account.json.json'

cliente = bigquery.Client()

sql_query = """
SELECT nombre, id, clasificacion, precio, fecha_de_salida, stock
FROM `sanguine-orb-379207.Juegos.Games` LIMIT 1000
"""

query_job = cliente.query(sql_query)

# Crea una plantilla HTML utilizando jinja2
template = Template('''
<html>
    <head>
        <title>Resultado de la consulta de BigQuery</title>
    </head>
    <body>
        <table>
            {% for row in rows %}
            <tr>
                {% for value in row.values() %}
                <td>{{ value }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </body>
</html>
''')

# Genera el resultado HTML utilizando la plantilla y los datos de la consulta de BigQuery
result_html = template.render(rows=query_job.result())

# Escribe el resultado en un archivo HTML
with open('resultado.html', 'w') as f:
    f.write(result_html)
