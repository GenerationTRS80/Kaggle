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

tblTrips = dataset_ref.table("taxi_trips")
df = client.list_rows(tblTrips, max_results=50).to_dataframe()

print(df.head())

sSQL = """ WITH TaxiTrips AS (
            SELECT EXTRACT(YEAR FROM trip_start_timestamp) as Year, COUNT(taxi_id) as num_trips
            FROM 'bigquery-public-data.chicago_taxi_trips.taxi_trips'
            )
        """ + '\n\r'

sSQL = sSQL + """ SELECT Year, num_trips""" + '\n\r'
sSQL = sSQL + """ FROM TaxiTrips""" + '\n\r'
# sSQL = sSQL + """ WHERE  """ + '\n\r'
sSQL = sSQL + """ Group By Year """ + '\n\r'
sSQL = sSQL + """ Order By Year"""

print(sSQL)

# Setup query cancel if more data is used that set with safe_config
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
dfTrips = client.query(sSQL, job_config=safe_config).to_dataframe()

print(dfTrimps.head())
