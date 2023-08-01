"""Testing framework for unit testing in Python"""
import unittest
from tkinter import Tk
from calculator import Calculator

"""simulate user input and verify the expected output"""


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.calculator = Calculator()

    """Execute after each test method. It cleans up any resources that were created during the tests, in this case, 
    it destroys the Tkinter window. """
    def tearDown(self):
        self.root.destroy()

    def test_addition(self):
        # Test basic addition
        self.calculator.add_to_expression(3)
        self.calculator.append_operator('+')
        self.calculator.add_to_expression(5)
        self.calculator.evaluate()
        self.assertEqual(self.calculator.current_expression, "8")

        # Test decimal addition
        self.calculator.clear()
        self.calculator.add_to_expression(2.5)
        self.calculator.append_operator('+')
        self.calculator.add_to_expression(1.5)
        self.calculator.evaluate()
        self.assertEqual(self.calculator.current_expression, "4.0")

    def test_subtraction(self):
        # Test basic subtraction
        self.calculator.add_to_expression(8)
        self.calculator.append_operator('-')
        self.calculator.add_to_expression(5)
        self.calculator.evaluate()
        self.assertEqual(self.calculator.current_expression, "3")

        # Test decimal subtraction
        self.calculator.clear()
        self.calculator.add_to_expression(5.5)
        self.calculator.append_operator('-')
        self.calculator.add_to_expression(1.5)
        self.calculator.evaluate()
        self.assertEqual(self.calculator.current_expression, "4.0")

    def test_multiplication(self):
        self.calculator.add_to_expression(4)
        self.calculator.append_operator('*')
        self.calculator.add_to_expression(6)
        self.calculator.evaluate()
        self.assertEqual(self.calculator.current_expression, "24")

    def test_division(self):
        self.calculator.add_to_expression(15)
        self.calculator.append_operator('/')
        self.calculator.add_to_expression(3)
        self.calculator.evaluate()
        self.assertEqual(float(self.calculator.current_expression), 5.0)

        # Test division by zero
        self.calculator.clear()
        self.calculator.add_to_expression(10)
        self.calculator.append_operator('/')
        self.calculator.add_to_expression(0)
        self.calculator.evaluate()
        self.assertEqual(self.calculator.current_expression, "Error")

    def test_square(self):
        self.calculator.add_to_expression(5)
        self.calculator.square()
        self.assertEqual(self.calculator.current_expression, "25")

    def test_sqrt(self):
        self.calculator.add_to_expression(25)
        self.calculator.sqrt()
        self.assertEqual(float(self.calculator.current_expression), 5.0)

    def test_clear(self):
        self.calculator.add_to_expression(2)
        self.calculator.append_operator('+')
        self.calculator.add_to_expression(3)
        self.calculator.clear()
        self.assertEqual(self.calculator.current_expression, "")
        self.assertEqual(self.calculator.total_expression, "")


"""Check if the script is being run as the main program and not imported as a module. If it's the main program, 
it runs the test suite using unittest.main(). """
if __name__ == "__main__":
    unittest.main()
