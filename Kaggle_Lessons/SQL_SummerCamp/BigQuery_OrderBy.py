from google.cloud import bigquery
import pandas as pd

# Updated July 16 2019 9:30 PM

print('Version Pandas = ', pd.__version__)
print('BigQuery = ', bigquery.__version__)

# Create client object
client = bigquery.Client()

# Construct a reference to the "world_bank_intl_education" dataset
dataset_ref = client.dataset(
    "world_bank_intl_education", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# Get the list of tables
tbl_List = list(client.list_tables(dataset))

print('\n\r', ' ', 'List of tables in World Bank International Education', '\n\r', ' ')
for tblName in tbl_List:
    print(tblName.table_id)

# Construct a reference to the "international_education" table
table_ref = dataset_ref.table("international_education")

# API request - fetch the table
table = client.get_table(table_ref)

print('\n\r', ' ', 'Selected able Name = ', table.table_id, '\n\r', ' ')

for field in table.schema:
    print('Field Name = ', field.name)

df = client.list_rows(table, max_results=5).to_dataframe()


print(df)
print('Min year', df['year'].min())

#  >>> Use return a query to a dataframe with Bigquery <<<s

# Set up the query (cancel the query if it would use too much of
# your quota, with the limit set to 1 GB)

sSQL = """
            SELECT year, country_name, country_code, SUM(value)
            FROM `bigquery-public-data.world_bank_intl_education.international_education`
            WHERE country_code='UZB'
            GROUP BY year, country_name, country_code
            ORDER BY year
        """
# print(sSQL)

# Retrieve BigQuery data as a Pandas DataFrame
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10 ** 10)
dfQry = client.query(sSQL, job_config=safe_config).to_dataframe()

print(dfQry.head())
