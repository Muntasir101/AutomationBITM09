import unittest


def setup():
    print("Setup DONE")



class testModule(unittest.TestCase):
    def test_case1(self):
        print("Test Case 1 DONE")

    def test_case2(self):
        print("Test Case 2 DONE")


if __name__ == "__main__":
    unittest.main()


def teardown():
    print("Test Complete")