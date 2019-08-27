# Exercises

hello = "hello\n\rworld"
print(hello)

# >> Strings are sequences

# Indexing
planet = 'Pluto'
print(planet[0])

# Last 3 characters and first 3 characters
print(planet[-3:])
print(planet[:3])

# char comprehesion loop
list = [char + '!' for char in planet]
print(list)

# String methonds
# ALL CAPS
strText = "Pluto is a planet"
print(strText.upper())

# Searching for the first index of a substring
print('First Index = ', strText.index('plan'))
print('Start with planet ', strText.startswith('planet'))


# Going between strings and lists
words = strText.split()
print(words)

# Yes, we can put unicode characters right in our string literals :)
sString = ' 👏 '.join([word.upper() for word in words])
print(sString)

# str.split() turns a string into a list of smaller strings, breaking on whitespace by default.
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print('Year '+year + ' Month '+month+' Day '+day)

print('/'.join([year, month, day]))

# Concatenate
sConcatenate = planet + ' we, miss you'
print(sConcatenate)

intPosition = 9
sConcatenate = planet + ' You will always be the ' + \
    str(intPosition) + 'th planet to me'
print(sConcatenate)

#Format .format()
# call .format() on a "format string", where the Python values we want to insert are represented with {} placeholders.

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

#     2 decimal points   3 decimal points, format as percent     separate with commas
strPlutoMass = "{} weights about {: .2} kilograms ({: .3%} of earths mass). It's home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population)

print(strPlutoMass)

# Referring to format() arguments by index, starting from 0
s = """Pluto's as {0}. No, it's a {1}.
No. it's a {1}.{0}!{1}!""" .format('planet', 'dwarf planet')
print(s)

# Dictionaries
# data structure for mapping keys to values.

numbers = {'one': 1, 'two': 2, 'three': 3}

# dictionary comprehensions with a syntax similar to the list comprehensions

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

# in operator tells us whether something is a key in the dictionary
print('Saturn' in planet_to_initial)
print('Betelgeuse' in planet_to_initial)

for k in numbers:
    print("{}={}".format(k, numbers[k]))

# access a collection of all the keys or all the values with dict.keys() and dict.values()
# Get all the initials, sort them alphabetically, and put them in a space-separated string.

tmpInitial = ''.join(sorted(planet_to_initial.values()))
print(tmpInitial)
