"""
Sample tests
"""


from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding two numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_add_numbers_negative(self):
        """Test adding two negative numbers together."""
        res = calc.add(-5, -6)

        self.assertEqual(res, -11)

    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)

    def test_subtract_negative_numbers(self):
        """Test subtracting two numbers."""
        res = calc.subtract(-10, -5)

        self.assertEqual(res, -5)
