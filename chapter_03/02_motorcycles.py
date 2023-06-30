motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# append new element
motorcycles.append('kawasaki')
print(motorcycles)

# insert new element at first position
motorcycles.insert(0, 'bmw')
print(motorcycles)

# remove last item in the list
removed = motorcycles.pop()
print(f"removed last: {removed}; list: {motorcycles}")

# remove 2nd item in the list
removed = motorcycles.pop(1)
print(f"removed 2nd: {removed}; list: {motorcycles}")

# remove by value
motorcycles.remove('bmw')
print(motorcycles)