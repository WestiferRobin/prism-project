
def convert_celsius_to_fahrenheit(celsius: float):
    fahrenheit = ((9/5) * celsius) + 32
    return fahrenheit

def convert_celsius_to_kelvin(celsius: float):
    kelvin = celsius + 273.15
    return kelvin

def convert_fahrenheit_to_celsius(fahrenheit: float):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

def convert_fahrenheit_to_kelvin(fahrenheit: float):
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    kelvin = convert_celsius_to_kelvin(celsius)
    return kelvin

def convert_kelvin_to_celsius(kelvin: float):
    celsius = kelvin - 273.15
    return celsius

def convert_kelvin_to_fahrenheit(kelvin: float):
    celsius = convert_kelvin_to_celsius(kelvin)
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return fahrenheit
