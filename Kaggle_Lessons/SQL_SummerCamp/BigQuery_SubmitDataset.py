# https://google-cloud.readthedocs.io/en/latest/bigquery/usage.html

from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

datasets = list(client.list_datasets())
project = client.project

if datasets:
    print('Datasets in project {}:'.format(project))
    for dataset in datasets:  # API request(s)
        print('\t{}'.format(dataset.dataset_id))
else:
    print('{} project does not contain any datasets.'.format(project))
