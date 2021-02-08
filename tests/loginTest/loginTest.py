from utilities.util import Util
from pages.loginPage.login_page import LoginPage
from pages.mainMenuPage.mainMenuPage import MainMenuPage
from utilities.testStatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_csv import getCSVData
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@ddt
@pytest.mark.usefixtures("getWebdriver")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, getWebdriver):
        log = cl.customLogger(logging.DEBUG)
        self.loginPage = LoginPage(self.driver)
        self.mainPage = MainMenuPage(self.driver)
        self.util = Util()
        self.testStatus = TestStatus(self.driver)

    @data(*getCSVData("loginDatas.csv"))
    @unpack
    def test_login(self, emailAddress, pw, testType):
        self.testStatus.mark(self.loginPage.isLoginBtnVisible(), resultMessage="Login button visibility check")
        self.loginPage.enterCredentials(emailAddress, pw)
        self.loginPage.clickLoginBtn()
        if testType == "valid":
            self.testStatus.markFinal(testName="testValidLogin", result=self.loginPage.checkLoginSuccessfull(),
                                      resultMessage="Login successfuly check")
        if testType == "invalid":
            self.testStatus.markFinal(testName="Alert appear", result=self.loginPage.alertContentCheck(),
                                      resultMessage="Alert appear")
        if testType == "emptyField":
            self.testStatus.markFinal(testName="Empty fields test", result=self.loginPage.emptyFieldAlertMessageCheck(),
                                      resultMessage="Alert appear")
        if testType == "emailFormat":
            self.testStatus.markFinal(testName="Password format test", result=self.loginPage.passwordFormatAlertMessageCheck(),
                                      resultMessage="Alert appear")

