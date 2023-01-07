import unittest

class Login(unittest.TestCase):
    def test_login_email(self):
        print("Login by Email")

    def test_login_gmail(self):
        print("Login by Gmail")

    def test_login_facebook(self):
        print("Login by Facebook")

if __name__ == "__main__":
    unittest.main()