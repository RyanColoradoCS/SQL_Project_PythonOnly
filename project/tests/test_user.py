# python3 -m unittest discover -s project/tests

import unittest
from project.models import User, Admin, Customer, BankAccount

# Import the global variable from models
import project.models as models

class TestUser(unittest.TestCase):

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

    
if __name__ == '__main__':
    unittest.main()
