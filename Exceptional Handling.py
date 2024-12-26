def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except Exception as e:
        print("An error occurred during the conversion:", e)

# Example usage:
temperature_fahrenheit = 75
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
if temperature_celsius is not None:
    print(f"{temperature_fahrenheit}°F is equal to {temperature_celsius:.2f}°C")






def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the formula
    return (fahrenheit - 32) * 5 / 9

# Task 1: Ask the user to input the temperature in Fahrenheit
user_input = input("Please enter the temperature in Fahrenheit: ")

try:
    # Task 2: Attempt to convert the input to a number (Fahrenheit)
    fahrenheit = float(user_input)  # Try to convert the input to a float
    
    # Task 3: Convert to Celsius and print the result in a user-friendly format
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")

except ValueError:
    # If the user enters a non-numeric value, handle the error
    print(f"Error: '{user_input}' is not a valid number. Please enter a valid numeric value.")

finally:
    # Task 4: Display the thank you message
    print("Thank you for using the weather forecast application.")
