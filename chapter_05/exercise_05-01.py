# 5-1. Conditional Tests: 
# Write a series of conditional tests. Print a statement describing each test
# and your prediction for the results of each test. Your code should look
# something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# - Look closely at your results, and make sure you understand why each line
#   evaluates to True or False.
# - Create at least 10 tests. Have at least 5 tests evaluate to True and another
#   5 tests evaluate to False.

family = ['stefan', 'georg', 'marion', 'helga']
print('Is Helga a family member? I predict True.')
print('helga' in family)

print('Is Thomas a family member? I predict False.')
print('thomas' in family)

l_limit = 18
u_limit = 65

age = 12
print(f"Is {age} inside age limits? I predict False.")
print(l_limit <= age and age <= u_limit)

age = 72
print(f"Is {age} inside age limits? I predict False.")
print(l_limit <= age and age <= u_limit)

age = 32
print(f"Is {age} inside age limits? I predict True.")
print(l_limit <= age and age <= u_limit)


age = 12
print(f"Is {age} off limits? I predict True.")
print( age < l_limit or age > u_limit)

age = 72
print(f"Is {age} off limits? I predict True.")
print( age < l_limit or age > u_limit)

age = 32
print(f"Is {age} off limits? I predict False.")
print( age < l_limit or age > u_limit)

