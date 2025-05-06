
#Function To Convert Celcius To Fahrenheit
def convertCelsiusToFahrenheit (temperatureInC):
    temperatureInF = ((9/5) * temperatureInC ) + 32
    return temperatureInF

#Function To Fahrenheit  To Celcius
def convertFahrenheitToCelcius (temperatureInF):
    temperatureInC = (5/9) * (temperatureInF - 32)
    return temperatureInC

# Main function
def main():
    print("Temperature Conversion Tool")
    try:
        choice = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").strip().upper()
        
        if choice == "C":
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp}°C is {convertCelsiusToFahrenheit(temp):.2f}°F")
        
        elif choice == "F":
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp}°F is {convertFahrenheitToCelcius(temp):.2f}°C")
        
        else:
            print("Invalid choice. Please enter 'C' or 'F'.")
    
    except Exception as e:
        print(f"Error:{e}")

# Run the main function
while True:
    main()
    again = input("\nDo you want to do another conversion? (y/n): ").strip().lower()
    if again != 'y':
        print("Thank you for using the Temperature Conversion Tool. Goodbye!")
        break



