import unittest

from users import User


class UserTests(unittest.TestCase):

    def test_creating_a_user(self):
        user = User("bob", "password")
        self.assertEqual(repr(user), "User(bob, Normal)")
        self.assertEqual(str(user), "bob")
