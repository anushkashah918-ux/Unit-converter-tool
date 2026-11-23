
def length_converter():
    print("\n--- LENGTH CONVERTER ---")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Centimeters to Meters")
    print("4. Meters to Centimeters")
    print("5. Miles to Kilometers")
    print("6. Kilometers to Miles")

    choice = input("Choose conversion: ")

    try:
        value = float(input("Enter value: "))

        conversions = {
            "1": (value / 1000, "kilometers"),
            "2": (value * 1000, "meters"),
            "3": (value / 100, "meters"),
            "4": (value * 100, "centimeters"),
            "5": (value * 1.60934, "kilometers"),
            "6": (value / 1.60934, "miles")
        }

        if choice in conversions:
            result, unit = conversions[choice]
            print(f"Result: {result:.4f} {unit}")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")


def weight_converter():
    print("\n--- WEIGHT CONVERTER ---")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")

    choice = input("Choose conversion: ")

    try:
        value = float(input("Enter value: "))

        conversions = {
            "1": (value * 1000, "grams"),
            "2": (value / 1000, "kilograms"),
            "3": (value * 2.20462, "pounds"),
            "4": (value / 2.20462, "kilograms")
        }

        if choice in conversions:
            result, unit = conversions[choice]
            print(f"Result: {result:.4f} {unit}")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")


def temperature_converter():
    print("\n--- TEMPERATURE CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose conversion: ")

    try:
        value = float(input("Enter temperature: "))

        conversions = {
            "1": (value * 9/5 + 32, "Fahrenheit"),
            "2": ((value - 32) * 5/9, "Celsius"),
            "3": (value + 273.15, "Kelvin"),
            "4": (value - 273.15, "Celsius")
        }

        if choice in conversions:
            result, unit = conversions[choice]

            if choice in ("3", "4") and result < 0:
                print("Invalid temperature below absolute zero!")
            else:
                print(f"Result: {result:.2f} {unit}")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")


def time_converter():
    print("\n--- TIME CONVERTER ---")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Minutes to Hours")
    print("4. Hours to Minutes")
    print("5. Hours to Seconds")
    print("6. Seconds to Hours")

    choice = input("Choose conversion: ")

    try:
        value = float(input("Enter value: "))

        conversions = {
            "1": (value / 60, "minutes"),
            "2": (value * 60, "seconds"),
            "3": (value / 60, "hours"),
            "4": (value * 60, "minutes"),
            "5": (value * 3600, "seconds"),
            "6": (value / 3600, "hours")
        }

        if choice in conversions:
            result, unit = conversions[choice]
            print(f"Result: {result:.4f} {unit}")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n================================")
        print("       UNIT CONVERTER TOOL")
        print("================================")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Time Conversion")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            time_converter()
        elif choice == "5":
            print("Thank you for using Unit Converter!")
            break
        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
