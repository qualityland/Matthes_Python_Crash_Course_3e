guests = ['johann sebastian bach', 'john coltrane', 'corey fujimoto']

print(f'Unfortunately {guests[-1].title()} can\'t make it.')

guests[-1] = 'kalei gamiao'

for guest in guests:
    print(f'Dear {guest.title()}, I would like to invite you to dinner.')