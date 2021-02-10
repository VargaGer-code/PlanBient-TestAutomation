from base.basepage import BasePage
from utilities.testStatus import TestStatus
from utilities.util import Util
from pages.loginPage.login_page import LoginPage
from pages.registerPage.register_page import RegistrationPage
from ddt import ddt, data, unpack
from utilities.read_csv import getCSVData
import utilities.custom_logger as cl
import unittest
import pytest
import logging

@ddt
@pytest.mark.usefixtures("getWebdriver")
class RegistrationTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, getWebdriver):
        log = cl.customLogger(logging.DEBUG)
        self.loginPage = LoginPage(self.driver)
        self.registerPage = RegistrationPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.util = Util()
        self.testStatus = TestStatus(self.driver)

    @data(*getCSVData("tests/registerTest/registerDatas.csv"))
    @unpack
    def registration(self, emailDDT, regTypeDDT, fullNameDDT, phoneDDT, ps1DDT, ps2DDT, companyNameDDT, taxNumDDT, postCodeDDT, cityDDT, streetDDT, contactEmailDDT):
        self.loginPage.clickRegisterBtn()
        self.testStatus.mark(self.registerPage.isRegisterBtnPresent(), resultMessage="Register button visibility check")
        self.registerPage.fillRegistrationForm(email=emailDDT, regType=regTypeDDT,
                                            fullName=fullNameDDT, phone=phoneDDT, ps1=ps1DDT, ps2=ps2DDT,
                                            companyName=companyNameDDT, taxNum=taxNumDDT, postCode=postCodeDDT,
                                            city=cityDDT, street=streetDDT, contactEmail=contactEmailDDT)
        self.registerPage.clickAszfBtn()
        self.registerPage.clickRegistrationBtn()
        self.testStatus.markFinal("Registration test", result=self.registerPage.registrationSuccessfulCheck(), resultMessage="Registration successful check")

    @data(*getCSVData("tests/registerTest/validateAlertMsg.csv"))
    @unpack
    def test_checkAlertMessages(self, elementLocator, dataToCheck, alertMsg, resultMessage):
        self.loginPage.clickRegisterBtn()
        self.registerPage.fillInputField(elementLocator, dataToCheck)
        self.registerPage.clickAszfBtn()
        self.registerPage.clickRegistrationBtn()
        self.testStatus.mark(resultMessage=resultMessage, result=self.registerPage.isAlertVisible(elementLocator, alertMsg))
        self.registerPage.clickLoginPageBtn()
        self.testStatus.markFinal(testName="Check alert messages", result=self.loginPage.isLoginBtnVisible(), resultMessage=resultMessage)

    def registerBtnDisplayed(self):
        self.loginPage.clickRegisterBtn()
        self.registerPage.webScrollToElement(self.registerPage._registrationBtn)
        self.testStatus.mark(result=not self.registerPage.isRegisterBtnEnabled(), resultMessage="Register Btn is enabled")
        self.registerPage.clickAszfBtn()
        self.testStatus.mark(result=self.registerPage.isRegisterBtnEnabled(), resultMessage="Register Btn is NOT enabled")
        self.registerPage.clickAszfBtn()
        self.testStatus.markFinal(testName="Register btn enabled test", result=not self.registerPage.isRegisterBtnEnabled(), resultMessage="Register Btn NOT is enabled")
        self.registerPage.clickLoginPageBtn()













