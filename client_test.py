import unittest
from client3 import getDataPoint, getRatio

# Intern: Nicolas Huang
# 8/11/2023
# Task 1 - JPMC Virtual Internship


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_EmptyQuote(self):
    quote = []
    with self.assertRaises(ValueError):
      stock, bid_price, ask_price, price = getDataPoint(quote)

  def test_getRatio(self):
    self.assertEqual(getRatio(2.90, 1.45), 2.00)

  def test_getRatio_DivideZero(self):
    self.assertIsNone(getRatio(3.00, 0))

  def test_getRatio_NegativePrice(self):
    self.assertIsNone(getRatio(5.44, -2.00))


def main():
  try:
    unittest.main()
  except:
    raise


if __name__ == '__main__':
    main()
