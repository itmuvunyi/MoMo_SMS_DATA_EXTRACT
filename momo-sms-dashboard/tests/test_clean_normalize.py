# import unittest
# from etl.clean_normalize import clean_amount, normalize_date, normalize_phone

# class TestCleanNormalize(unittest.TestCase):

#     def test_clean_amount(self):
#         self.assertEqual(clean_amount("1,234.56"), 1234.56)
#         self.assertEqual(clean_amount("$1,234.56"), 1234.56)
#         self.assertEqual(clean_amount("1234.56"), 1234.56)
#         self.assertEqual(clean_amount("invalid"), None)

#     def test_normalize_date(self):
#         self.assertEqual(normalize_date("2023-10-01"), "2023-10-01")
#         self.assertEqual(normalize_date("01/10/2023"), "2023-10-01")
#         self.assertEqual(normalize_date("10-01-2023"), "2023-10-01")
#         self.assertEqual(normalize_date("invalid"), None)

#     def test_normalize_phone(self):
#         self.assertEqual(normalize_phone("+1234567890"), "1234567890")
#         self.assertEqual(normalize_phone("(123) 456-7890"), "1234567890")
#         self.assertEqual(normalize_phone("123-456-7890"), "1234567890")
#         self.assertEqual(normalize_phone("invalid"), None)

# if __name__ == '__main__':
#     unittest.main()