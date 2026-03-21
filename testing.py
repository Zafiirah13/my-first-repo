"""This is a test file for testing purposes."""
class Operation:
    def __init__(self, c, d):
        self.c = c
        self.d = d
        self.result = None

    def divide(self):
        if self.d != 0:
            self.result = self.c / self.d
        else:
            return "Division by zero is not allowed."

    def multiply(self):
        return self.c * self.d

Class LinearEquation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def solve(self):
        if self.a != 0:
            return -self.b / self.a
        else:
            return "Coefficient a cannot be zero for a linear equation."