# https://google-cloud.readthedocs.io/en/latest/bigquery/usage.html#tables
# Import BigQuery
from google.cloud import bigquery

# Create Client object
client = bigquery.Client()

# Construct a reference to "hacker news" dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

# API fetch - dataset
dataset = client.get_dataset(dataset_ref)

# list tables
tables = list(client.list_tables(dataset))

tbl_print = ''

for table in tables:
    #tbl_print = table.table_id + ' ' + table.description
    # print(int=tab)
    print(table.table_id)
    # print(table.description)

# Construct a reference to the "comments" table
table_ref = dataset_ref.table('comments')

# API request - fetch the table
tbl_comments = client.get_table(table_ref)
print('table name', tbl_comments.table_id + '\n\r' + 'carriage return')

# Preview the first five lines of the "comments" table
print(client.list_rows(tbl_comments, max_results=5).to_dataframe())

# Query to select prolific commenters and post counts
prolific_commenters_query = """
        SELECT author, COUNT(1) AS NumPosts
        FROM `bigquery-public-data.hacker_news.comments`
        GROUP BY author
        HAVING COUNT(1) > 10000
        """  # Your code goes here

query_del = """
        SELECT deleted, COUNT(id) AS NumPosts
        FROM `bigquery-public-data.hacker_news.comments`
       Where deleted = TRUE
       Group By deleted
        """  # Your code goes here


# Set up the query (cancel the query if it would use too much of
# your quota, with the limit set to 1 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**9)
query_job = client.query(prolific_commenters_query, job_config=safe_config)

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**9)
query_del_job = client.query(query_del, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
prolific_commenters = query_job.to_dataframe()
print(prolific_commenters)

# API request - run the query, and return a pandas DataFrame
deleted_comments = query_del_job.to_dataframe()
print(deleted_comments)
