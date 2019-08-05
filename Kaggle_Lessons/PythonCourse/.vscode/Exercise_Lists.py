# # Lists in Python represent ordered sequences of values. Here is an example of how to create them:

# primes = [2, 3, 5, 7]

# planets = ['Mercury', 'Venus', 'Earth', 'Mars',
#            'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# # make a list of lists:

# hands = [
#     ['J', 'Q', 'K'],
#     ['2', '2', '2'],
#     ['6', 'A', 'K'],  # (Comma after the last element is optional)
# ]
# # (I could also have written this on one line, but it can get hard to read)
# hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]


# # mix of different types of variables:
# my_favourite_things = [32, 'raindrops on roses', help]
# print(my_favourite_things)


# print(planets[0])
# print(planets[1])
# print('Planets furthest from the sun', planets[-1])
# print('First 3 planets', planets[0:3])
# print('Last 5 planets', planets[3:])
# print('Last 3 planets', planets[-3:])

# # Negative indices
# # All the planets except the first and last
# print(planets[1:-1])

# # modify a list is to assign to an index or slice expression.
# planets[3] = 'Malacandra'
# print('Rename Mars to Malacandra', planets)


# planets[:3] = ['Mur', 'Vee', 'Ur']
# print(planets)
# # That was silly. Let's give them back their old names
# planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars', ]

# # Use carraige return "\n\r"
# print("Set List of planets"+'\n\r', planets)

# # How many planets are there?
# print(len(planets))

# # The planets sorted in alphabetical order
# sort_planets = sorted(planets)
# print('Sort planets A-Z', sort_planets)

# # sum
# primes = [2, 3, 5, 7]
# print('Total = ', sum(primes))
# print('Max = ', max(primes))

# # #Interlude: Objects
# # I've used the term 'object' a lot so far - you may have even read that everything in Python is an object. What does that mean?

# # In short, objects carry some things around with them. You access that stuff using Python's dot syntax.
# # For example, numbers in Python carry around an associated variable called imag representing their imaginary part. (You'll probably never need to use this unless you're doing some very weird math.)

# x = 12
# # x is a real number, so its imaginary part is 0.
# print(x.imag)

# # Here's how to make a complex number, in case you've ever been curious:
# c = 12 + 3j
# print(c.imag)

# # Is Earth a planet?
# planet_exists = "Earth" in planets
# print(planet_exists)

# Exercises

# def select_second(L):
#     """Return the second element of the given list. If the list has no second
#     element, return None.
#     """
#     if len(L) < 2:
#         return None
#     return L[1]


# L = [1, 2, 3]


# print(select_second(L))


# # Exercise 2

# def losing_team_captain(teams):
#     """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
#     from the last listed team
#     """
#     team = teams[-1]
#     return team[1]
#     pass


# Giants = ['Bochy', 'Posey', 'MadBum']
# Dbacks = ['Torey Lovullo', 'Paul Goldschmidt']
# Dodgers = ['Dave Roberts', 'Clayton Kershaw']

# teams = [Giants, Dbacks, Dodgers]

# print(losing_team_captain(teams))

# # Exercise 3
# def purple_shell(racers):

#     racer_first = racers[0]
#     racer_last = racers[-1]
#     racers[0] = racer_last
#     racers[-1] = racer_first

#     return racers


# r = ["Mario", "Bowser", "Luigi"]

# print(purple_shell(r))

# # Exercise 4

# a = [1, 2, 3]
# b = [1, [2, 3]]
# c = []
# d = [1, 2, 3][1:]

# print(len(d))

# Exercise 5

def fashionably_late(arrivals, name=''):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """

   # arrival_wo_Last = arrivals[:len(arrivals)-1]
    half = (len(arrivals)//2)+1
    arrivals.pop()
    # return half
    return arrivals[half:]


party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

print(fashionably_late(party_attendees, 'May'))
