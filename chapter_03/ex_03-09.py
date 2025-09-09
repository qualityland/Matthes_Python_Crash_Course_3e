guests = ['johann sebastian bach', 'john coltrane', 'corey fujimoto']

print(guests)
print(len(guests))


guests.insert(0, 'miles davis')
guests.insert(2, 'don cherry')
guests.append('wayne shorter')

print(guests)
print(len(guests))

guests.pop(-2)
guests.pop(0)
guests.pop(0)
guests.pop(0)

print(guests)
print(len(guests))