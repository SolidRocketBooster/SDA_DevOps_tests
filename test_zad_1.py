from unittest import TestCase
from zad_1 import minimum

class MinimumTest(TestCase):

    def setUp(self):
        self.l_int = [3, 4, 6, 1]
        self.l_str = ['spam', 'foobar', 'bar']
        self.l_float = [1.4, 11.6, 0.2, 0.0]
        self.l_mix = ['spam', 3, 2.4]

    def test_int(self):
        self.assertEqual(minimum(self.l_int), 1)
        self.assertIs(type(minimum(self.l_int)), int)

    def test_float(self):
        self.assertEqual(minimum(self.l_float), 0.0)
        self.assertIs(type(minimum(self.l_float)), float)

    def test_string(self):
        self.assertEqual(minimum(self.l_str), 'bar')
        self.assertIs(type(minimum(self.l_str)), str)

    def test_mix(self):
        self.assertEqual(minimum(self.l_mix), "'<' not supported between instances of 'float' and 'str'")

