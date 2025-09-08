# import unittest
# from etl.categorize import categorize_transaction

# class TestCategorize(unittest.TestCase):

#     def test_categorize_income(self):
#         transaction = {'amount': 100, 'description': 'Salary'}
#         category = categorize_transaction(transaction)
#         self.assertEqual(category, 'Income')

#     def test_categorize_expense(self):
#         transaction = {'amount': -50, 'description': 'Groceries'}
#         category = categorize_transaction(transaction)
#         self.assertEqual(category, 'Expense')

#     def test_categorize_transfer(self):
#         transaction = {'amount': 0, 'description': 'Transfer to savings'}
#         category = categorize_transaction(transaction)
#         self.assertEqual(category, 'Transfer')

#     def test_categorize_unknown(self):
#         transaction = {'amount': 10, 'description': 'Unknown transaction'}
#         category = categorize_transaction(transaction)
#         self.assertEqual(category, 'Unknown')

# if __name__ == '__main__':
#     unittest.main()