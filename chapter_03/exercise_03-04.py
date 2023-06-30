# 03-04. Guest List:
# If you could invite anyone, living or deceased, to dinner, who would you
# invite? Make a list that includes at least three people you’d like to invite
# to dinner. Then use your list to print a message to each person, inviting them
# to dinner.

guests = ['robert plant', 'john bonham', 'jimmy page', 'john paul johnes']

for g in guests:
    print(f"Hi {g.title()}, I'd like to invite you to dinner!")