# 03-08. Seeing the World:
# Think of at least five places in the world you’d like to visit.
# - Store the locations in a list. Make sure the list is not in alphabetical
#   order.
places = ['mexico', 'china', 'australia', 'new zealand', 'canada']

# - Print your list in its original order. Don’t worry about printing the list
#   neatly; just print it as a raw Python list.
print(f"original:\t\t{places}")

# - Use sorted() to print your list in alphabetical order without modifying the
#   actual list.
print(f"temp. sorted:\t\t{sorted(places)}")

# - Show that your list is still in its original order by printing it.
print(f"original:\t\t{places}")

# - Use sorted() to print your list in reverse-alphabetical order without
#   changing the order of the original list.
print(f"temp. rev sort:\t\t{sorted(places, reverse=True)}")

# - Show that your list is still in its original order by printing it again.
print(f"original:\t\t{places}")

# - Use reverse() to change the order of your list. Print the list to show that
#   its order has changed.
places.reverse()
print(f"reversed:\t\t{places}")

# - Use reverse() to change the order of your list again. Print the list to show
#   it’s back to its original order.
places.reverse()
print(f"2nd reverse:\t\t{places}")

# - Use sort() to change your list so it’s stored in alphabetical order.
#   Print the list to show that its order has been changed.
places.sort()
print(f"perm. sorted:\t\t{places}")

# - Use sort() to change your list so it’s stored in reverse-alphabetical order.
#   Print the list to show that its order has changed.
places.sort(reverse=True)
print(f"perm. rev sort:\t\t{places}")