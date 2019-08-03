# Lists in Python represent ordered sequences of values. Here is an example of how to create them:

primes = [2, 3, 5, 7]

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# make a list of lists:

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],  # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]


# mix of different types of variables:
my_favourite_things = [32, 'raindrops on roses', help]
print(my_favourite_things)


print(planets[0])
print(planets[1])
print('Planets furthest from the sun', planets[-1])
print('First 3 planets', planets[0:3])
print('Last 5 planets', planets[3:])
print('Last 3 planets', planets[-3:])

# Negative indices
# All the planets except the first and last
print(planets[1:-1])

# modify a list is to assign to an index or slice expression.
planets[3] = 'Malacandra'
print('Rename Mars to Malacandra', planets)


planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars', ]

# Use carraige return "\n\r"
print("Set List of planets"+'\n\r', planets)

# How many planets are there?
print(len(planets))

# The planets sorted in alphabetical order
sort_planets = sorted(planets)
print('Sort planets A-Z', sort_planets)

# sum
primes = [2, 3, 5, 7]
print('Total = ', sum(primes))
print('Max = ', max(primes))

# #Interlude: Objects
# I've used the term 'object' a lot so far - you may have even read that everything in Python is an object. What does that mean?

# In short, objects carry some things around with them. You access that stuff using Python's dot syntax.
# For example, numbers in Python carry around an associated variable called imag representing their imaginary part. (You'll probably never need to use this unless you're doing some very weird math.)

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)
