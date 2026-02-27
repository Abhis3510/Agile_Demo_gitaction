# 3.Pyunit Lab
import unittest
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(104, self.calc.add(3, 101), "The addition is wrong")

    def test_subtract(self):
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)