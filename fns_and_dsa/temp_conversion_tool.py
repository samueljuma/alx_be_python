# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32


def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET


def main():

    try:
        # User input for temperature
        temp_input = float(input("\nEnter the temperature to convert: ").strip())
    except ValueError:
        print("\nInvalid temperature. Only numbers are accepted.\n")
        return

    # Ask user for temperature unit (Celsius or Fahrenheit)
    unit = (
        input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    )

    if unit == "C":
        # Convert from Celsius to Fahrenheit
        fahrenheit_temp = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {fahrenheit_temp}°F \n")
    elif unit == "F":
        # Convert from Fahrenheit to Celsius
        celsius_temp = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {celsius_temp}°C \n")
    else:
        print("\nInvalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit. \n")


if __name__ == "__main__":
    main()
