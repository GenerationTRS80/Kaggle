from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

# Create reference to the dataset
dataset_ref = client.dataset("openaq", project="bigquery-public-data")

# Get dataset
dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))

for table in tables:
    print(table.table_id)
