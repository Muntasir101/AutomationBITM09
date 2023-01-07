import unittest

from Framework.Login.test_login import Login
from Framework.Purchase.test_order import PurchaseCourse
from Framework.Registration.test_register import Register
from Framework.Deposite.test_deposit import Deposit
from UnitTest.TestSuite.login_smoke_test import test_suite
import HtmlTestRunner


class TestSuite(unittest.TestCase):
    def test_suite(self):
        self.test1 = unittest.TestLoader().loadTestsFromTestCase(Login)
        self.test2 = unittest.TestLoader().loadTestsFromTestCase(Register)
        self.test3 = unittest.TestLoader().loadTestsFromTestCase(PurchaseCourse)
        self.test4 = unittest.TestLoader().loadTestsFromTestCase(Deposit)

        smoke_test_suite = unittest.TestSuite([self.test1, self.test2, self.test3])
        sanity_test_suite = unittest.TestSuite([self.test1])

        runner = HtmlTestRunner.HTMLTestRunner(output="F:\\SQA\\Batch09\\AutomationBITM09\\Framework\\Reports\\TestReport")
        #runner.run(smoke_test_suite)

        runner.run(sanity_test_suite)



if __name__ == "__main__":
    test_suite()
    #unittest.main()
