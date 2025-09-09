guests = ['johann sebastian bach', 'john coltrane', 'corey fujimoto']

for guest in guests:
    print(f'Dear {guest.title()}, I found a bigger table for our dinner.')

guests.insert(0, 'miles davis')
guests.insert(2, 'don cherry')
guests.append('wayne shorter')

for guest in guests:
    print(f'Dear {guest.title()}, I would like to invite you to dinner.')

print('I\'m so sorry, but I can only invite two people!')

print(guests)

print(f'Sorry {guests.pop(-2).title()}!')
print(f'Sorry {guests.pop(0).title()}!')
print(f'Sorry {guests.pop(0).title()}!')
print(f'Sorry {guests.pop(0).title()}!')

for guest in guests:
    print(f'Dear {guest.title()}, I would like to invite you to dinner.')