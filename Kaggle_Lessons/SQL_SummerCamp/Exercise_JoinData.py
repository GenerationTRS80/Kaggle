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

# Query dataframe

questions_query = """
                    Select id, title, owner_user_id
                    From `bigquery-public-data.stackoverflow.posts_questions`
                    Where tags LIKE '%bigquery%'
                  """

# Set up the query (cancel the query if it would use too much of
# your quota, with the limit set to 1 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10 ** 10)
questions_query_job = questions_query

# API request - run the query, and return a pandas DataFrame
questions_results = client.query(
    questions_query_job, job_config=safe_config).to_dataframe()

print(questions_results.head())
