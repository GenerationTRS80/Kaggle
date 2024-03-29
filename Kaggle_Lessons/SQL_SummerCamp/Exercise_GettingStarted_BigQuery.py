from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

# Client Object properties
clientTProjects = client.list_projects

# for project in clientTProjects:
#     print(project)

# Construct a reference to the "chicago_crime" dataset
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")
#dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)


# Write the code you need here to figure out the answer
tables = list(client.list_tables(dataset))

for table in tables:
    print(table.table_id)


# Construct a reference to the "full" table
table_ref = dataset_ref.table("crime")

# API request - fetch the table
table = client.get_table(table_ref)

# # Print information on all the columns in the "full" table in the "hacker_news" dataset
# schema = table.schema

for field in table.schema:
    print(field.name)

# Preview the first five lines of the "full" table
print(client.list_rows(table, max_results=5).to_dataframe())

# # Preview the first five entries in the "by" column of the "full" table
# client.list_rows(
#     table, selected_fields=table.schema[:1], max_results=5).to_dataframe()
