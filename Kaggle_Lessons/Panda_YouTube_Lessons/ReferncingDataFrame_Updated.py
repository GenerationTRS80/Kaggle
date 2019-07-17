# https://www.youtube.com/watch?v=te5JrSCW-LY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=34
# read the drinks dataset into DataFrame
import pandas as pd

# read drinks dataset into dataframe
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')


print(pd.__version__)
print(drinks.head())

# Find the number of drinks servered for Anagola
print('Drinks served in Angola = ', drinks.loc['Angola', 'spirit_servings'])

# Find an alternate reference for iloc
print('Drinks served in Angola = ', drinks.loc['Angola', drinks.columns[1]])

# alternative use iloc
print('Use drink index', drinks.iloc[drinks.index.get_loc('Angola'), 1])
