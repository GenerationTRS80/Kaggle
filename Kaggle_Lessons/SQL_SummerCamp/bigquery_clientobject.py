from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

dataset_ref = client.dataset()

dateset = client.get_dataset(dataset_ref)
