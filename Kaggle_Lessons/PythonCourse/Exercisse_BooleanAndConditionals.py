# Booleans
x = True
print(x)
print(type(x))


def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must "have attained to the Age of thirty-five Years"
    return age >= 35


print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))


#  check if a number is odd by checking that the modulus with 2 returns 1
a = 100
b = 7


def is_odd(n):
    return (n % 2) == 1


print("Is " + str(a) + " odd?", is_odd(a))
print("Is " + str(b) + " odd?", is_odd(b))

# Combining boolean values


def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)


print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

# .>>> Conditionals <<<<
# Note you need to indent for this statement to works
a = 33
b = 200
if b > a:
    print("b is greater than a")  # you will get an error

# Boolean converstion
print(bool(1))  # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf"))  # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

# elif
if 0:
    print(0)
elif "spam":
    print("spam")


# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 3300
b = 330
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
elif a > b:
    print("a and b are equal")
else:
    print('Not found')

# two values depending on some condition is a pretty common pattern


def quiz_message(grade):
    if grade < 50:
        outcome = 'failed'
    else:
        outcome = 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)


quiz_message(80)

#  >>>>>   Exercise  <<<<<
