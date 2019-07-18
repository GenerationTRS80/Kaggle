from google.cloud import bigquery

# Create a Client Object
client = bigquery.Client()

# Construct reference to the chicago taxi trips
dataset_ref = client.dataset(
    "chicago_taxi_trips", project="bigquery-public-data")

# API request - fetch datasets
dataset = client.get_dataset(dataset_ref)

# Get list of tables
tables = list(client.list_tables(dataset))

table_name = ''

# Get table names
for table in tables:
    table_name = table.table_id
    print(table_name)

    # Get table ref
    table_ref = dataset_ref.table(table_name)
    objTable = client.get_table(table_ref)

    # Get field names
    for field in objTable.schema:
        print(field.name)
