# 03-05. Changing Guest List:
# You just heard that one of your guests can’t make the dinner, so you need to
# send out a new set of invitations. You’ll have to think of someone else to
# invite.
# - Start with your program from Exercise 3-4. Add a print() call at the end of
#   your program, stating the name of the guest who can’t make it.
# - Modify your list, replacing the name of the guest who can’t make it with the
#   name of the new person you are inviting.
# - Print a second set of invitation messages, one for each person who is still
#   in your list.

guests = ['robert plant', 'john bonham', 'jimmy page', 'john paul johnes']
print(f"Unfortunately {guests[1].title()} cannot make it!")

guests[1] = "ronald shannon jackson"
for guest in guests:
    print(f"Hi {guest.title()}, I'd like to invite you to dinner!")