# Addition function
def add(a, b):
    return a + b


# Subtraction function
def subtract(a, b):
    return a - b


# Multiplication function
def multiply(a, b):
    return a * b


# Division function
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Function to read valid numbers
def read_number(message):
    while True:
        try:
            number = float(input(message))
            return number

        except ValueError:
            print("Invalid input! Please enter a number.")

# Conversion factors
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


# Kilometres to miles
def km_to_miles(km):
    return km * CONVERSION_FACTORS["km_to_miles"]


# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Kilograms to pounds
def kg_to_pounds(kg):
    return kg * CONVERSION_FACTORS["kg_to_pounds"]

def unit_converter():

    while True:

        print("\n====== UNIT CONVERTER ======")
        print("1. Kilometres to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            km = read_number("Enter kilometres: ")
            print("Miles:", km_to_miles(km))

        elif choice == "2":
            celsius = read_number("Enter Celsius: ")
            print("Fahrenheit:", celsius_to_fahrenheit(celsius))

        elif choice == "3":
            kg = read_number("Enter kilograms: ")
            print("Pounds:", kg_to_pounds(kg))

        elif choice == "4":
            break

        else:
            print("Invalid choice! Select between 1 and 4.")

def main():

    while True:

        print("\n================================")
        print("     INTERACTIVE CALCULATOR")
        print("================================")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Converter")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "6":
            print("Thank you for using the calculator!")
            break

        elif choice in ("1", "2", "3", "4"):

            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")

            if choice == "1":
                print("Result:", add(a, b))

            elif choice == "2":
                print("Result:", subtract(a, b))

            elif choice == "3":
                print("Result:", multiply(a, b))

            elif choice == "4":
                print("Result:", divide(a, b))

        elif choice == "5":
            unit_converter()

        else:
            print("Invalid choice! Please select between 1 and 6.")
if __name__ == "__main__":
    main()