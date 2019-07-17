from google.cloud import bx`igquery

# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "chicago_crime" dataset
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")

dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))

# Construct a reference to the "full" table
table_ref = dataset_ref.table("crime")

# API request - fetch the table
table = client.get_table(table_ref)

# # Count the number of fields with TIMESTAMP type
# print(sum(table.field_type == "TIMESTAMP" for table in table.schema))

num_timestamp_fields = 0
field_names = ''

for field in table.schema:
    if (field.field_type == 'TIMESTAMP'):
        num_timestamp_fields += 1
        field_names = field_names + field.name + "\n\r"
print("Number of fields with TIMESTAMP", num_timestamp_fields)
print(field_names)

# for field in table.field:
#     print(field.name)

# Preview the first five lines of the "full" table
print(client.list_rows(table, max_results=5).to_dataframe())


# Write the code to figure out the answer
fields_for_plotting = ''

for field in table.schema:
    if (field.field_type == 'FLOAT'):
        fields_for_plotting = fields_for_plotting + field.name + "\r\n"

print(fields_for_plotting)
