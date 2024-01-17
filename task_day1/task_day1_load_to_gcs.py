from google.cloud import storage
import os

def write_to_gcs(bucket_name, blob_name, data):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data)

bucket_name = os.getenv('BUCKET_NAME')
blob_name = 'task_day1_load.json'

data = '[\
{"name": "karno punta", "age": 26, "pekerjaan": "data engineer", "Alamat": "Pontianak, Kalimantan Barat", "tgl_lahir": "1997-10-14"},\
{"name": "elon musk", "age": 24, "pekerjaan": "data scientist", "Alamat": "Jakarta, DKI Jakarta", "tgl_lahir": "1999-10-14"},\
{"name": "deki deka", "age": 23, "pekerjaan": "mahasiswa", "Alamat": "Banjarmasin, Kalimantan Selatan", "tgl_lahir": "2000-10-14"}\
]'
write_to_gcs(bucket_name, blob_name, data)
