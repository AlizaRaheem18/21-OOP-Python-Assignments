"""
Assignment:
Create a class Logger that prints
 a message when an object is created (constructor) and another message when it is destroyed (destructor)."""

class Logger:
    def __init__(self):
        print("Object Created") #constructor

    def __del__(self):
        print("Object Destroyed") #destructor


if __name__ == "__main__":
    log = Logger()
    del log 
