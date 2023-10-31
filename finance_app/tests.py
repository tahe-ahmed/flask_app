import finance_app
import unittest
from finance_app.home.index import calculate_holdings

class MyTestCase(unittest.TestCase):

    def setUp(self):
        finance_app.testing = True
        
    def test_calculate_holdings(self):
        # Define mock buy and sell transactions
        buy_transactions = [('AAPL', 2, 170.27), ('TSLA', 4, 197.305)]
        sell_transactions = [('AAPL', 1, 170.27), ('TSLA', 2, 197.305)]

        # Call the calculate_holdings function
        holdings = calculate_holdings(buy_transactions, sell_transactions)

        # Assert the expected results
        self.assertEqual(holdings['AAPL']['shares'], 1)
        self.assertAlmostEqual(float(holdings['AAPL']['total_price'][1:]), 170.27)
        self.assertEqual(holdings['TSLA']['shares'], 2)
        self.assertAlmostEqual(float(holdings['TSLA']['total_price'][1:]), 394.61)

    def test_calculate_holdings_buy_only(self):
        # Test case with buy transactions only
        buy_transactions = [('AAPL', 2, 170.27), ('TSLA', 4, 197.305)]
        sell_transactions = []  

        holdings = calculate_holdings(buy_transactions, sell_transactions)

        self.assertEqual(holdings['AAPL']['shares'], 2)
        self.assertAlmostEqual(float(holdings['AAPL']['total_price'][1:]), 340.54)
        self.assertEqual(holdings['TSLA']['shares'], 4)

    def test_calculate_holdings_sell_only(self):
        # Test case with sell transactions only
        buy_transactions = [] 
        sell_transactions = [('AAPL', 2, 170.27), ('TSLA', 4, 197.305)]

        holdings = calculate_holdings(buy_transactions, sell_transactions)

        self.assertEqual(holdings, {})  

    def test_calculate_holdings_no_transactions(self):
        # Test case with no buy or sell transactions
        buy_transactions = [] 
        sell_transactions = [] 

        holdings = calculate_holdings(buy_transactions, sell_transactions)

        self.assertEqual(holdings, {})  
        
        
    def test_calculate_holdings_buy_sell_equal(self):
        # Test case with buy and sell transactions that balance out
        buy_transactions = [('AAPL', 2, 170.27), ('TSLA', 4, 197.305)]
        sell_transactions = [('AAPL', 2, 170.27), ('TSLA', 4, 2800.0)]

        holdings = calculate_holdings(buy_transactions, sell_transactions)

        self.assertEqual(holdings, {})  


