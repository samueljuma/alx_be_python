def perform_operation(num1, num2, operation):
    if operation == "add":
        return f"{num1 + num2}"
    elif operation == "subtract":
        return f"{num1 - num2}"
    elif operation == "multiply":
        return f"{num1 * num2}"
    elif operation == "divide":
        if num2 == 0:
            return "You cannot divide by zero."
        else:
            return f"{num1 / num2}"
    else:
        return "Invalid operation"
