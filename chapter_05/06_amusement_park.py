age = 12

if age < 4:
    print("Your admission costs $0.")
elif age < 18:
    print("Your admission costs $25.")
else:
    print("Your admission costs $40.")


# better alternative

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
