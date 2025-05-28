"""
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
"""
class TempratureConverter():
    @staticmethod
    def celsius_to_fahrenheit(c):
        return(c * 9 /5 ) + 32
    
if __name__ == "__main__":
    print("Fahrenheit:",TempratureConverter.celsius_to_fahrenheit(0))
    print("Fahrenheit:",TempratureConverter.celsius_to_fahrenheit(100))