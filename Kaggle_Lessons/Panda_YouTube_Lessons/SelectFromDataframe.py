import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
#drinks = Spd.read_csv('http://bit.ly/drinksbycountry')
#movies = pd.read_csv('http://bit.ly/imdbratings')
#train = pd.read_csv('http://bit.ly/kaggletrain')
#ufo = pd.read_csv('http://bit.ly/uforeports', parse_dates=['Time'])

head1 = ufo.head(3).drop('Time', axis=1)

# You can print data results
# print(head1)

# print(ufo[ufo.City == 'Oakland'])

# Use loc to get all rows with Oakland as city
print(ufo.loc[ufo.City == 'Oakland', :])
