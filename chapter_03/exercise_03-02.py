# 03-02. Greetings:
# Start with the list you used in Exercise 03-01, but instead of just printing
# each person’s name, print a message to them. The text of each message should
# be the same, but each message should be personalized with the person’s name.

names = ['helga', 'marion', 'georg', 'moritz', 'evi', 'benno']

for n in names:
    print(f"Hi {n.title()}, wie geht's?")