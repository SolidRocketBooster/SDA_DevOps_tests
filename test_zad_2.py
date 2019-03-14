from unittest import TestCase
from zad_2 import palindrom

class TestPalindrom(TestCase):
    def setUp(self):
        self.word1 = 'kajak'
        self.word2 = 'spam'
        self.int1 = 101

    def test_true(self):
        self.assertEqual(palindrom(self.word1), True)

    def test_false(self):
        self.assertEqual(palindrom(self.word2), False)

    def test_int(self):
        self.assertRaises(palindrom(self.int1), "'int' object is not subscriptable")

    def test_none(self):
        self.assertRaises(palindrom(None), "'NoneType' object is not subscriptable")
