import unittest
from unittest.mock import patch
import sys
import os
from src.scripts.converter import fetch_exchange_rates, get_exchange_rate


class TestConverter(unittest.TestCase):

    @patch('src.scripts.converter.requests.get')
    def test_fetch_exchange_rate_success(self, mock_get):
        mock_get.return_value.json.return_value = {"rates": {"USD": 1.12}}
        rate = get_exchange_rate("USD")
        self.assertEqual(rate, 1.12)

    @patch('src.scripts.converter.requests.get')
    def test_fetch_exchange_rate_failure(self, mock_get):
        mock_get.side_effect = Exception("API failure")
        rate = get_exchange_rate("USD")
        self.assertIsNone(rate)


if __name__ == '__main__':
    unittest.main()
