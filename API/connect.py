import datetime
from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime
from google.cloud import bigquery
import os

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'API/clouddemo-service-account.json.json'
cliente = bigquery.Client()

# Metodo Retrieve All
@app.route('/')
def index():
    sql_query = """
    SELECT nombre, id, clasificacion, precio, fecha_de_salida, stock
    FROM `sanguine-orb-379207.Juegos.Games` LIMIT 1000
    """

    query_job = cliente.query(sql_query)
    rows = [dict(row) for row in query_job.result()]

    return render_template('Home.html', rows=rows)

#Metodo Post

@app.route('/insertar', methods=['POST'])
def insert():
    nombre = request.form['nombre']
    id = request.form['id']
    clasificacion = request.form['clasificacion']
    precio = request.form['precio']
    fecha_de_salida = request.form['fecha_de_salida']
    stock = request.form['stock']

    # Convertir el precio a un entero
    try:
        precio = int(precio)
    except ValueError:
        precio = None
    
    # Crear un objeto datetime a partir de la fecha
    fecha_de_salida = datetime.strptime(fecha_de_salida, '%Y-%m-%dT%H:%M')

    insert_data = [(nombre, int(id), clasificacion, precio, fecha_de_salida, stock)]
    table = cliente.get_table('sanguine-orb-379207.Juegos.Games')
    errors = cliente.insert_rows(table, insert_data)

    if errors == []:
        message = 'Datos insertados correctamente.'
    else:
        message = 'Error al insertar los datos. Inténtelo de nuevo.'

    return render_template('Home.html', message=message)

# Metodo Delete
@app.route('/eliminar', methods=['POST'])
def delete():
    id = request.form['id']

    # Create a reference to the table
    table_ref = cliente.dataset('Juegos').table('Games')
    table = cliente.get_table(table_ref)

    # Delete rows based on the ID
    delete_query = "DELETE FROM sanguine-orb-379207.Juegos.Games WHERE id = {}".format(id)
    query_job = cliente.query(delete_query)
    result = query_job.result()

    return redirect('/')


# Metodo Update
@app.route('/actualizar', methods=['POST'])
def update():
    # Leer los datos del formulario
    id = request.form['id']
    nombre = request.form['nombre']
    clasificacion = request.form['clasificacion']
    precio = request.form['precio']
    fecha_de_salida = request.form['fecha_de_salida']
    stock = int(request.form['stock'])

    # Crear un objeto datetime a partir de la fecha
    fecha_de_salida = datetime.strptime(fecha_de_salida, '%Y-%m-%dT%H:%M')

    # Ejecutar la consulta SQL para actualizar la fila
    update_query = """
    UPDATE `sanguine-orb-379207.Juegos.Games`
    SET nombre = '{}', clasificacion = '{}', precio = '{}', fecha_de_salida = DATETIME('{}'), stock = CAST({} AS INT64)
    WHERE id = {}
    """.format(nombre, clasificacion, str(precio), fecha_de_salida, stock, id)

    query_job = cliente.query(update_query)
    result = query_job.result()

    return redirect('/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
