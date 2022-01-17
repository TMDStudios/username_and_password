import unittest
import username_and_password

class TestUsernameAndPassword(unittest.TestCase):

    def test_name_available(self):
        # Should only return true if name is not in users list ['Sam', 'Frank', 'Jane']
        self.assertFalse(username_and_password.name_available('Sam'))
        self.assertFalse(username_and_password.name_available('Jane'))
        self.assertTrue(username_and_password.name_available('Richard'))

    def test_number_found(self):
        # Return true if name contains a number
        self.assertFalse(username_and_password.number_found('Bob'))
        self.assertTrue(username_and_password.number_found('Bob3'))
        self.assertTrue(username_and_password.number_found('Ab4c'))

    def test_caps_found(self):
        # Return true if name contains an uppercase letter
        self.assertFalse(username_and_password.caps_found('tim'))
        self.assertTrue(username_and_password.caps_found('Tim'))
        self.assertTrue(username_and_password.caps_found('tiM'))

    def test_special_found(self):
        # Return true if name contains a special character ['!', '@', '#', '$']
        self.assertFalse(username_and_password.special_found('tim'))
        self.assertFalse(username_and_password.special_found('Tim'))
        self.assertTrue(username_and_password.special_found('Tim!'))

    def test_username_added_to_users(self):
        # Should return true if username has been added to users list
        self.assertTrue(username_and_password.username in username_and_password.users)