first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# can f-strings actually include newlines?
# only if started with 3 double quotes.
message2 = f"""Here starts an f-string
including a newline. stop."""
print(message2)