from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """
        Confirm that one and one is two
        """
        self.assertEqual(add(1, 1), 2)

    def test_subtract_numbers(self):
        """
        Test that values are subtracted correctly and returned
        """
        self.assertEqual(subtract(7, 4), 3)
