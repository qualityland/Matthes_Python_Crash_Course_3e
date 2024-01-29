# 02-07. Stripping Names:
# Use a variable to represent a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions
# - lstrip()
# - rstrip()
# - strip()
print("Note: Begining and end of the string including whitespace are marked with '<' and '>'.")
name = "     \t        Stefan    \t   \t  \n    "
print("<" + name + ">")
print("<" + name.lstrip() + ">")
print("<" + name.rstrip() + ">")
print("<" + name.strip() + ">")

