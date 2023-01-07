import unittest

class Signup(unittest.TestCase):
    def test_signup_email(self):
        print("signup by Email")

    def test_signup_gmail(self):
        print("signup by Gmail")

    def test_signup_facebook(self):
        print("signup by Facebook")

if __name__ == "__main__":
    unittest.main()