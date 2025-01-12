from datetime import datetime, timedelta


# Part 1: Display the Current Date and Time
def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current Date and Time: {formatted_date}")


# Part 2: Calculate a Future Date
def calculate_future_date():
    """
    Calculates and displays a future date based on user input of number of days.
    """
    try:
        # Prompt the user to enter the number of days
        number_of_days = int(input("Enter the number of days to add to the current date:"))
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=number_of_days)  # Calculate future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"The date after {number_of_days} days will be: {formatted_future_date}\n")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Main Function
def main():
    """
    Main function to execute the script.
    """
    print()
    display_current_datetime()  # Display the current date and time
    calculate_future_date()  # Calculate and display a future date


if __name__ == "__main__":
    main()
