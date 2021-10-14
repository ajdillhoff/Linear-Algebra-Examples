"""
first.py
This is a Python program which covers basic input, output, exception handling,
and conditional statements.

Note the the start and end sequence to indicate multi-line comments.
"""

str1 = "World!"
str2 = "Everyone!"

# Read input from the user (a single line comment)
choice = input("Enter either 0 or 1: ")

# Attempt to convert to an integer
try:
    choice = int(choice)
except:
    print(f'\"{choice}\" is not a number. Defaulting to 0')
    choice = 0

if int(choice) == 0:
    print(f'Hello {str1}')
elif int(choice) == 1:
    print(f'Hello {str2}')
else:
    print('{choice} is not a valid input.')
