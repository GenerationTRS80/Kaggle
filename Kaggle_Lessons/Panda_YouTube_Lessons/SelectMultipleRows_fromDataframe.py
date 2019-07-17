import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.head(3))

# # Find things by labels using the loc command
# ufo.loc[1:2, :]
# print(ufo.loc[0:2])


# # All Rows and city column
# print(ufo.loc[:, ['City', 'State']].head(5))

# # Show all columns except time
# print('Show all columns except time')
# print(ufo.head(3).drop('Time', axis=1))

# Select city of oakland
print(ufo.loc[ufo.City == 'Oakland', 'State'])

# Select by columns and rows by reference
ufo.iloc[:, 0:4]
