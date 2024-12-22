#Prompt user to enter two numbers first number and second number
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Prompt user to enter an operation
operation = input("Choose the operation (+, -, *, /): ").strip() #strip() removes any leading or trailing whitespace

# Perform the calculation based on the operation- Use match case
match operation:
  case "+":
    result = first_number + second_number
  case "-":
    result = first_number - second_number
  case "*":
    result = first_number * second_number
  case "/":
    #Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.
    if second_number == 0:
        print("You cannot divide by zero.")
        result = None
    else:
      result = first_number / second_number

#Display the result of the operation in a user-friendly message, e.g., The result is [result].
if result is not None:
  print(f"The result is {result}.")
