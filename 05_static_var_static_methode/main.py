"""
Assignment:
Create a class MathUtils with a static method 
add(a, b) that returns the sum. No class or instance variables should be used.
"""

class MathUtils:

    @staticmethod
    def add(a,b):
       return a+b

if __name__ == "__main__":
    result = MathUtils.add(3,5)
    print("Sum:",result)