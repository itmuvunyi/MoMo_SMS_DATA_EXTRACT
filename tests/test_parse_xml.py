# import unittest
# from etl.parse_xml import parse_xml

# class TestParseXML(unittest.TestCase):

#     def test_parse_valid_xml(self):
        
#         transactions = parse_xml('data/raw/momo.xml')
#         self.assertIsInstance(transactions, list)
#         self.assertGreater(len(transactions), 0)

#     def test_parse_invalid_xml(self):
        
#         with self.assertRaises(Exception):
#             parse_xml('data/raw/invalid_momo.xml')

#     def test_transaction_structure(self):
#         transactions = parse_xml('data/raw/momo.xml')
#         for transaction in transactions:
#             self.assertIn('amount', transaction)
#             self.assertIn('date', transaction)
#             self.assertIn('phone', transaction)

# if __name__ == '__main__':
#     unittest.main()