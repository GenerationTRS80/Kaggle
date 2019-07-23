from google.cloud import bigquery

# Create client object
client = bigquery.Client()

# Construct a reference to the "stackoverflow" dataset
dataset_ref = client.dataset("stackoverflow", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# #Get list of tables
# tables = list(client.list_tables(dataset))

# list_of_tables = [table.table_id for table in tables]
# print(list_of_tables)

# for table in tables:
#     print(table.table_id)

table_ref = dataset_ref.table('posts_answers')
tblReturned = client.get_table(table_ref)

# Print fields
print(tblReturned.table_id)

# tblReturned_Fields = [field.name for field in tblReturned.schema]
# print(tblReturned_Fields)

for field in tblReturned.schema:
    print(field.name)

df = client.list_rows(tblReturned, max_results=5).to_dataframe()

print(df)
