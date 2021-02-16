import unittest
from tests.loginTest.loginTest import LoginTest
from tests.mainMenuTest.mainMenuTest import MainMenuTest
# from tests.mediasTest.mediasTest import MediasTest
# from tests.registerTest.registerTest import RegistrationTest

# Getting test cases from test classes
loginTestCases = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
mainMenuTestCases = unittest.TestLoader().loadTestsFromTestCase(MainMenuTest)

# Creating a test suit by combining all the test cases
test = unittest.TestSuite([loginTestCases, mainMenuTestCases])

# Running test
unittest.TextTestRunner(verbosity=2).run(test)
