alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original posistion [x, y]: {alien_0['x_position']}, {alien_0['y_position']}")

# move alien to the right
# determine how far to move the alien based on it's current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

alien_0['x_position'] += x_increment

print(f"New position [x, y]: {alien_0['x_position']}, {alien_0['y_position']}")

# remove a key-value pair
print(alien_0)
del alien_0['y_position']
print(alien_0)