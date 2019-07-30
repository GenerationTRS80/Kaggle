help(round(-2.01))

# The Sep argument is used for a seperator
print(1, 2, 3, sep=' < ')

# Create a function call it greet return the value you entered and hello


def greet(who='Colin'):
    print('Hello', who)


greet()
greet(who='Kaggle')
greet('Leon')

# Functions Applied to Functions


def multi_by_five(x):
    return 5 * x


def call(fn, arg):
    """ Call function on an argument"""
    return fn(arg)


def squared_call(fn, arg):
    """ Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(multi_by_five, 1),
    squared_call(multi_by_five, 1),
    sep='\n',  # '\n' is the newline character - it starts a new line
)


# Functions that operate on other funcitons
def mod_5(x):
    """Return the remainder after dividing by 5x"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which is the biggest modulo 5?'
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

>> > Exercises << <<
num = 3.14159


def round_to_two_places(num):
    """Return the given number rounded to two decimal places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)


print('Round 3.14159 to 2 places = ', round_to_two_places(num))

# Round to negative digits ie instead of 2 try -2
ndigits = -3
value = 333666
print('round ndigits', round(value, ndigits))


#  Function that will calculate the number of candies to smash for *any* number of total candies.
def to_smash(total_candies, numSmash=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    return total_candies % numSmash


print('Left over candies ', to_smash(305, 7))

# Which of the two variables above has the smallest absolute value?
x = -10
y = 5


def smallest_value(x, y):
    if abs(x) > abs(y):
        return y
        return x


smallest_abs = smallest_value(x, y)
print('Smallest absolute value = ', smallest_abs)
