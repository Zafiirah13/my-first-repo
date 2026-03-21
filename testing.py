"""This is a test file for testing purposes."""

# Function to add two numbers
def add(c, a, b):
    return c + a + b

def multiply(a, b):
    print("Multiplying numbers")
    return a * b

class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def subtract(self):
        return self.a - self.b
