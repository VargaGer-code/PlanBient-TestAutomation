from utilities.util import Util
from pages.loginPage.login_page import LoginPage
from pages.mainMenuPage.mainMenuPage import MainMenuPage
from pages.registerPage.register_page import RegistrationPage
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
        self.registerPage = RegistrationPage(self.driver)
        self.util = Util()
        self.testStatus = TestStatus(self.driver)

    @data(*getCSVData("C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\loginTest\\invalidLoginDatas.csv"))
    @unpack
    def test_invalid_login(self, emailAddressDDT, pwDDT, locatorDDT, alertMsgDDT):
        self.loginPage.login(emailAddressDDT, pwDDT)
        self.loginPage.clickLoginBtn()
        self.testStatus.mark(resultMessage="Invalid login validation",
                             result=self.registerPage.isAlertVisible(locatorDDT, alertMsgDDT))
        self.loginPage.clearCredentials()
        self.testStatus.markFinal(testName="Invalid login validation",
                                  result=self.loginPage.isLoginBtnVisible(),
                                  resultMessage="Invalid login validation")


    def test_passwordVisibilityCheck(self):
        self.loginPage.enterCredentials("Password is visible check", "Yo mamma")
        self.loginPage.screenShot(resultMessage="Password not visible")
        self.loginPage.clearCredentials()
        self.loginPage.enterCredentials("Password is visible check", "Yo mamma")
        self.loginPage.clickPasswordVisibilityBtn()
        self.loginPage.screenShot(resultMessage="Password visible")
