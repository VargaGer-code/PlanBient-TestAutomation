from base.basepage import BasePage
from utilities.testStatus import TestStatus
from utilities.util import Util
from pages.loginPage.login_page import LoginPage
from pages.mainMenuPage.mainMenuPage import MainMenuPage
from ddt import ddt, data, unpack
from utilities.read_csv import getCSVData
import utilities.custom_logger as cl
import unittest
import pytest
import logging

@ddt
@pytest.mark.usefixtures("getWebdriver")
class MainMenuTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, getWebdriver):
        log = cl.customLogger(logging.DEBUG)
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.mainMenu = MainMenuPage(self.driver)
        self.util = Util()
        self.testStatus = TestStatus(self.driver)

    @data(*getCSVData("tests/mainMenuTest/mainMenus.csv"))
    @unpack
    def test_validateUserProfiles(self, emailDDT, pwDDT, userNameDDT, userTypeDDT, mediasPageDDT, campaignPageDDT, ColleguesDDT, PartnersDDT):
        self.loginPage.login(emailDDT, pwDDT)
        self.testStatus.mark(self.loginPage.checkLoginSuccessfull(), "Login successful validation")
        self.mainMenu.openSettingsTopbar()
        self.mainMenu.openUserProfile()
        self.testStatus.mark(self.mainMenu.isProfileOpenedSuccesfully(), resultMessage="Profile page validation")
        self.testStatus.mark(self.mainMenu.checkUserName(userNameDDT), resultMessage="Username validation")
        self.testStatus.mark(self.mainMenu.checkUserType(userTypeDDT), resultMessage="User Type Validation")
        self.mainMenu.logout()
        self.testStatus.markFinal("User profile validation", result=self.loginPage.isLoginBtnVisible(), resultMessage="Login page validation failed")