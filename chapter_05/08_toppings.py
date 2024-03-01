requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print(f"Sorry, we ran out of {requested_topping} right now.")
        else:
            print(f"Adding {requested_topping}.")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")