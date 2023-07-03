my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# friend_foods = my_foods              # this does not work - copies a reference!!!

print("My favorite foods are:")
print(my_foods)

print("My friend's foods are:")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("My friend's foods are:")
print(friend_foods)
