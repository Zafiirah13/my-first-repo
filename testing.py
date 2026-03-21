"""This is a test file for testing purposes."""

def add(a, b):
    op_class = Operation(a,b)
    return op_class.add()

def multiply(a, b):
    op_class = Operation(a,b)
    return op_class.multiply()

def subtract(a,b):
    op_class = Operation(a,b)
    return op_class.subtract()

def divide(a,b):
    op_class = Operation(a,b)
    return op_class.divide()

class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        return
