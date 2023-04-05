from flask import Flask, render_template
from google.cloud import bigquery
import os

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'clouddemo-service-account.json.json'
cliente = bigquery.Client()

@app.route('/')
def index():
    sql_query = """
    SELECT nombre, id, clasificacion, precio, fecha_de_salida, stock
    FROM `sanguine-orb-379207.Juegos.Games` LIMIT 1000
    """

    query_job = cliente.query(sql_query)
    rows = [dict(row) for row in query_job.result()]

    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
