# Use a for loop to generate and print the multiplication
# table for a given number.

# Prompt the user to enter a number.
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
