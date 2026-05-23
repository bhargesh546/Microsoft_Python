
def main():
    temperature_c = float(input("Enter temperature in Celsius: "))
    temperature_f = float(input("Enter temperature in Farenheit: "))

    converted_f = convert_temperature(temperature_c, 'C')
    converted_c = convert_temperature(temperature_f, 'F')

    print(f"{temperature_c}°C is equal to {converted_f}°F")
    print(f"{temperature_f}°F is equal to {converted_c}°C")


def celsius_to_fahrenheit(celsius) -> float:
    tempereature_in_fahrenheit = (celsius * 9 / 5) + 32
    return tempereature_in_fahrenheit

def fahrenheit_to_celsius(fahrenheit)-> float:
    tempereature_in_celsius = (fahrenheit - 32) * 5 / 9
    return tempereature_in_celsius

def convert_temperature(temperature, unit):
    if unit.upper() == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit.upper() == 'F':
        return fahrenheit_to_celsius(temperature)
    
if __name__ == "__main__":
    main()