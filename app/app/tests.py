from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """
        Confirm that one and one is two
        """
        self.assertEqual(add(1, 1), 2)
