from unittest import TestCase
from funkcje import dziel

class TestDziel(TestCase):

    def setUp(self):
        self.wynik = dziel(1, 1)

    def tearDown(self):
        pass

    def test_two_positive_numbers(self):
        print(id(self.wynik))
        result = self.wynik
        self.assertEqual(result, 1)
        self.assertIs(type(result), float)

    def test_przez_zero(self):
        print(id(self.wynik))
        with self.assertRaises(ZeroDivisionError) as contex:
            dziel(1, 0)
        self.assertIs(ZeroDivisionError, type(contex.exception))


#  MOCK jest tez wazny
