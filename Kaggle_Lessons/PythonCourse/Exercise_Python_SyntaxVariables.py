a = [1, 2, 3]
b = [3, 2, 1]

tmp = a

# print(tmp)

a = b

#print('a =', a)

b = tmp

#print('b = ', b)

# Calculate extra candies

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies

Total = alice_candies + bob_candies + carol_candies
print('Total = ', Total)
to_smash = Total-((Total//3)*3)
print('Total Smash = ', to_smash)

print('Type = ', type(alice_candies))
print('Type to smash = ', type(to_smash))
