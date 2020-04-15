import unittest
from app.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_int(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_invalid_input_type(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")


if __name__ == "__main__":
    unittest.main()
