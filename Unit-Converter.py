while True:
    print("\n--- Unit Converter ---")
    print("1. Convert Kilometers to Miles")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km is equal to {miles:.2f} miles.")

    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
