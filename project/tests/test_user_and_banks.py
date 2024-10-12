# python3 -m unittest discover -s project/tests
# python3 -m unittest discover -s project/tests -v

import unittest
from project.models import User, Admin, Customer, BankAccount

# Import the global variable from models
import project.models as models

class TestUser(unittest.TestCase):
    print("Testing TestUser")
    def setUp(self):
        # Reset the global user_id to 0 before each test
        models.user_id = 0

    def test_user_creation(self):
        user = User("johndoe", "John Doe", "password123", "john@example.com")
        self.assertEqual(user.user_id, 1, "User ID should be 1")
        self.assertFalse(user.logged_in, "User should not be logged in by default")
        
        user = User("ryanyoung", "Ryan Young", "password123", "ryan.young@example.com")
        self.assertEqual(user.user_id, 2, "User ID should be 2")
        self.assertFalse(user.logged_in, "User should not be logged in by default")
    
    def test_login(self):
        user = User("johndoe", "John Doe", "password123", "john@example.com")
        user.login("password123")
        self.assertTrue(user.logged_in, "User should be logged in with correct password")

    def test_failed_login(self):
        user = User("Joe Smith", "Joe Smith", "password123", "joe.smith@example.com")
        user.login("wrongpassword")
        self.assertFalse(user.logged_in, "User should not be logged in with incorrect password")

    def test_logout(self):
        user = User("Joe Smith", "Joe Smith", "password123", "joe.smith@example.com")
        user.login("password123")
        user.logout()
        self.assertFalse(user.logged_in, "User should not be logged in after logging out")


class TestBank(unittest.TestCase):
    print("Testing TestBank")
    # Reset the global user_id to 0 before each test
    # Reset the global user_id to 0 before each test
    def setUp(self):
        models.account_id = 0
        models.user_id = 0

    def test_bank_account_creation_with_user(self):

        # create test user
        user = User("ryanyoung", "Ryan Young", "password123", "ryan.young@example.com")
        # Create a test bank account with a valid user
        account1 = BankAccount(user=user, bank_name="Ryan's Bank", account_number=12345678)
        self.assertEqual(account1.account_id, 1, "User ID should be 1")
        self.assertEqual(account1.user, user, "User should be the user passed in.")
        self.assertEqual(account1.bank_name, "Ryan's Bank", "Bank name should be 'Ryan's Bank'")
        self.assertEqual(account1.account_number, 12345678, "Account number should be 12345678")

    def test_bank_account_creation_with_no_user(self):
        # Test creating a bank account without a user and expect a ValueError
        '''
        The with statement is a replacement for commonly used try/finally error-handling statements. 
        A common example of using the with statement is opening a file.
        '''
        with self.assertRaises(ValueError) as context:
            BankAccount(user=None, bank_name="Test Bank", account_number="12345678")

        # Check that the error message is correct
        self.assertEqual(str(context.exception), "User cannot be None", "Error message should be 'User cannot be None'")

    
if __name__ == '__main__':
    unittest.main()
