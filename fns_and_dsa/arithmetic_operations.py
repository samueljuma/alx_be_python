def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return f"{num1 + num2}"
        case "subtract":
            return f"{num1 - num2}"
        case "multiply":
            return f"{num1 * num2}"
        case "divide":
            if num2 == 0:
                return "You cannot divide by zero."
            else:
                return f"{num1 / num2}"
              
        case _:
            return "Invalid operation"
