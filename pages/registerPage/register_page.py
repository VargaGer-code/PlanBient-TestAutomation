import utilities.custom_logger as cl
from base.basepage import BasePage
from utilities.util import Util
import logging


class RegistrationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ### Locators ###
    # Inputs
    _emailField = "//input[@name='email']"
    _registrationTypeDropDown = "//select[@name='roles']"
    _password1Field = "//input[@name='password']"
    _password2Field = "//input[@name='retyped_password']"

    _companyNameField = "//input[@name='company.name']"
    _taxNumField = "//input[@name='company.tax_number']"
    _postCodeField = "//input[@name='company.zip_code']"
    _cityField = "//input[@name='company.city']"
    _streetField = "//input[@name='company.street']"

    _fullNameField = "//input[@name='name']"
    _phoneNumberField = "//input[@name='phone_number']"
    _contact_email = "//input[@name='contact_email']"

    # Buttons
    _registrationBtn = "//button[@type='submit']"
    _loginPageBtn = "//a[@href='/login']"
    _aszfBtn = "//button[@class='toggle-btn__input-label']"

    # Alerts
    _registrationSuccessfulAlert = "//p[contains(text(), 'Sikeres regisztráció!')]"

    ### Actions ###
    def fillRegistrationForm(self, email, regType, fullName, phone, ps1, ps2, companyName, taxNum, postCode, city, street, contactEmail):
        self.sendKeys(email, self._emailField)
        self.selectFromDropdownByIndex(regType, self._registrationTypeDropDown, locatorType="xpath")
        self.sendKeys(ps1, self._password1Field)
        self.sendKeys(ps2, self._password2Field)
        self.sendKeys(companyName, self._companyNameField)
        self.sendKeys(taxNum, self._taxNumField)
        self.sendKeys(postCode, self._postCodeField)
        self.sendKeys(city, self._cityField)
        self.sendKeys(street, self._streetField)
        self.sendKeys(fullName, self._fullNameField)
        self.sendKeys(phone, self._phoneNumberField)
        self.sendKeys(contactEmail, self._contact_email)

    def fillInputField(self, elementLocator, dataToSend):
        self.sendKeys(data=dataToSend, locator=elementLocator, locatorType="xpath")

    def clickRegistrationBtn(self):
        self.elementClick(self._registrationBtn)

    def clickAszfBtn(self):
        self.elementClick(self._aszfBtn)

    def clickLoginPageBtn(self):
        self.elementClick(self._loginPageBtn)

    def isRegisterBtnEnabled(self):
        isRegisterBtnEnabled = self.isElementEnabled(self._registrationBtn)
        return isRegisterBtnEnabled

    def registrationSuccessfulCheck(self):
        isRegistrationSuccessfulAlertAppear = self.isElementPresent(self._registrationSuccessfulAlert)
        return isRegistrationSuccessfulAlertAppear

    def isRegisterBtnPresent(self):
        isRegisterBtnPresent = self.isElementPresent(self._registrationBtn)
        return isRegisterBtnPresent

    def isAlertVisible(self, alertOwnerElementLocator, alertMsg):
        """
        :param alertOwnerElementLocator: Locator with the result message belong
        :param alertMsg: Alert message to check
        :return: True if alert is visible ; False if alert is not visible
        """
        self.log.debug("alertOwnerElementLocator from file is :: " + str(alertOwnerElementLocator))
        self.log.debug("Alert msg from file is :: " + alertMsg)
        if self.isElementNotDisplayed(alertOwnerElementLocator + "//parent::div//span[contains(text(), '" + alertMsg + "')]") == True:
            return False
        else:
            isAlertVisible = self.isElementPresent(alertOwnerElementLocator + "//parent::div//span[contains(text(), '" + alertMsg + "')]")
            self.log.info("Element path is: //input[@name='" + alertOwnerElementLocator + "']//parent::div//span[contains(text(), '" + alertMsg + "')]")
            self.log.debug("isAlertPresent :: " + str(isAlertVisible))
        return isAlertVisible

    def isAlertNotVisible(self, alertOwnerElementLocator, alertMsg):
        if self.isElementNotDisplayed(alertOwnerElementLocator) is True:
            self.log.info("Element is NOT displayed")
        else:
            self.log.info("Element is displayed")












