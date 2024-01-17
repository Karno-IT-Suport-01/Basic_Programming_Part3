from google.cloud import bigquery
import os

def write_to_bigquery(table_id, data):
    client = bigquery.Client()
    table = client.get_table(table_id)
    for row in data:
        row['tgl_lahir'] += ' 00:00:00'
    errors = client.insert_rows(table, data)
    if errors:
        print('Terjadi kesalahan saat menyisipkan baris: {}'.format(errors))
    else:
        print('Berhasil menyisipkan data')

data = [
    {"name": "karno punta", "age": 26, "pekerjaan": "data engineer", "Alamat": "Pontianak, Kalimantan Barat", "tgl_lahir": "1997-10-14"},
    {"name": "elon musk", "age": 24, "pekerjaan": "data scientist", "Alamat": "Jakarta, DKI Jakarta", "tgl_lahir": "1999-10-14"},
    {"name": "deki deka", "age": 23, "pekerjaan": "mahasiswa", "Alamat": "Banjarmasin, Kalimantan Selatan", "tgl_lahir": "2000-10-14"}
]
project_id = os.getenv('PROJECT_ID')
table_id = f'{project_id}.my_dataset.task_table'
write_to_bigquery(table_id, data)
