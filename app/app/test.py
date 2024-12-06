"""
Sample Tests
"""

from django.test import SimpleTestCase
from rest_framework.test import APIClient
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_sub_numbers(self):
        """Test subtracting numbers together"""
        res = calc.subtract(6,5)
        self.assertEqual(res,1)