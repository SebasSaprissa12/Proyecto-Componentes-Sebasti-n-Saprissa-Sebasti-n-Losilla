import os 
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'clouddemo-service-account.json.json'

cliente = bigquery.Client()

sql_query = """
SELECT nombre, sexo, id 
FROM `sanguine-orb-379207.Juegos.Games` LIMIT 1000
"""

query_job = cliente.query(sql_query)

for row in query_job.result():
    print(row)