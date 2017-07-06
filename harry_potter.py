import unittest

PRICE = 8

class HarryPotter(unittest.TestCase):
    def test_single_book(self):
        quantities = [0,0,0,0,1]
        total = self.calc_price(quantities)
        expected_total = 8
        self.assertEqual(total, expected_total)

    def test_two_separate_books(self):
        quantities = [0,0,1,0,1]
        total = self.calc_price(quantities)
        expected_total = 15.2
        self.assertEqual(total, expected_total)

    def test_three_same_books(self):
        quantities = [0,0,3,0,0]
        total = self.calc_price(quantities)
        expected_total = 24
        self.assertEqual(total, expected_total)

    def test_price_total(self):
        quantities = [2,2,2,1,1]
        total = self.calc_price(quantities)
        expected_total = 51.6
        self.assertEqual(total, expected_total)

    def calc_price(self, quantities):
        total = 0
        while len(quantities) > 0:
            quantities = filter(lambda x: x != 0, quantities)
            length = len(quantities)
            print(quantities, length)
            discount = self.calc_discount(length)
            price_for_set = length*PRICE*discount
            total += price_for_set
            quantities = map(lambda x: x - 1, quantities)
        return total

    def calc_discount(self, length):
        if length == 0:
            return 0
        elif length == 1:
            return 1
        elif length == 2:
            return 0.95
        elif length == 3:
            return 0.9
        elif length == 4:
            return 0.8
        elif length == 5:
            return 0.75
        else:
            print(length)
            raise Exception
