import unittest


class PaymentTest(unittest.TestCase):
    def test_payment_cash(self):
        print("Payment by Cash Done")
        self.assertTrue(True)

    def test_payment_card(self):
        print("Payment by Card Done")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
