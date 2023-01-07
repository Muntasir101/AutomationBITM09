import unittest


class TestCaseDemo1(unittest.TestCase):

    def setup(self):
        print("Setup DONE")

    def test_case1(self):
        print("Test Case 1 Execute")

    def test_case2(self):
        print("Test Case 2 Execute")


if __name__ == "__main__":
    unittest.main()
