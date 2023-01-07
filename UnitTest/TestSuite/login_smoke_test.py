import unittest

from UnitTest.Package1 import loginTest


class test_suite(unittest.TestCase):
    test_case1 = unittest.TestLoader().loadTestsFromTestCase(loginTest.Login)

    smoke_test_suite = unittest.TestSuite([test_case1])

    unittest.TextTestRunner(smoke_test_suite)


if __name__ == "__main__":
    test_suite()
