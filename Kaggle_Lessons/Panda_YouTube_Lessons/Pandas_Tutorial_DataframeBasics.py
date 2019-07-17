import pandas as pd
import io
import os

# Add dataframe
# df = pd.read_csv(
#    '/users/micro/Documents/DataScience/Colab_Data/PG_listings.csv')
df = pd.read_csv(
    '../Panda_YouTube_Lessons/Data/PG_listings.csv')

# print(df.head(10))

# # Select columns to print
# print(df[['name', 'last_review', 'price']].head())

# # Get current working directory
# print(os.getcwd())

# # Get Columns
# print(df.columns)

# # Get type
# print(type(df['room_type']))

# Get Price
print(df['price'].head(10))
