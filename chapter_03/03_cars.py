cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"cars: {cars}")

# sort temporarily
print(f"temp. sorted: {sorted(cars)}")

# original order
print(f"original order: {cars}")

# reverse order
cars.reverse()
print(f"reversed order: {cars}")

# sort permanently
cars.sort(reverse=True)
print(f"sorted reverse: {cars}")