# Loops

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet, end=' ')  # print all on same line


# # Example 2 iterate over the elements of a tuple
# multiplicands = (2, 2, 2, 3, 3, 5)
# product = 1
# for mult in multiplicands:
#     product = product * mult
# print(product)

# # Example 3 loop through each character in a string:
# s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
# msg = ''
# print all the uppercase letters in s, one at a time
# for char in s:
#     if char.isupper():
#         print(char, end='')


# # Example function range()
# # range() is a function that returns a sequence of numbers
# for i in range(5):
#     print("Doing important work. i = ", i)

# # Example while loops
# i = 0
# while i < 10:
#     print(i, end=' ')
#     i += 1

# # Example  >>> List comprehensions <<<
# squares = [n**2 for n in range(10)]
# print('WITH comprehension', squares)

# squares = []
# for n in range(10):
#     squares.append(n**2)
# print('Without comprehension', squares)

# # Add a condition to the for loop
# short_planets = [planet for planet in planets if len(planet) < 6]
# print(short_planets)


# # str.upper() returns an all-caps version of a string
# loud_short_planets = [
#     planet.upper() + '!' for planet in planets if len(planet) < 6]
# print(loud_short_planets)

# # SQL analogy, you could think of these three lines as SELECT, FROM, and WHERE
# loud_short_planets = [
#     planet.upper() + '!'  # SELECT
#     for planet in planets  # FROM
#     if len(planet) < 6  # WHERE
# ]

# print(loud_short_planets)

# Count Negatves

def count_negatives(nums):
    return 'Count of negatives = ' + str(len([num for num in nums if num < 0]))


Listnum = [5, -1, -2, 0, 3]

print(count_negatives(Listnum))

# List compreshesion from list above


def count_negatives_wListComp(nums):
    return 'Count of negatives with List Compreshesion = ' + str(len([num for num in nums if num < 0]))


print(count_negatives_wListComp(Listnum))


# Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of
# Python where it calculates something like True + True + False + True to be equal to 3.
def count_negatives_bestmethod(nums):

    return 'Count of negatives best method = ' + str(sum([num < 0 for num in nums]))


print(count_negatives_bestmethod(Listnum))
