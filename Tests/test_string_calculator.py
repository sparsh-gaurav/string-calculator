import unittest
from src.string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
         self.assertEqual(add("1"), 1)

    def test_none_imput_add(self):
        self.assertEqual(add(None), 0)
        
    def test_multiple_numbers_add(self):
        self.assertEqual(add("1,5"), 6)

    def test_newline_and_comma_are_treated_as_delimiters(self):
         self.assertEqual(add("1\n2,3"), 6)
    
    def test_custom_delimiter_in_the_add_method(self):
         self.assertEqual(add("//;\n1;2"), 3)

if __name__ == "__main__":
    unittest.main()