import utilities.custom_logger as cl
from base.basepage import BasePage
from utilities.util import Util
import logging


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ### Locators ###
    # Login screen buttons
    _loginBtn = "//button[@type='submit']"
    _registerBtn = "//a[@href='/register']"
    _forgotPassword = "//a[contains(text(),'Elfelejtette jelszavát?')]"
    _passwordVisibilityBtn = "//button[@class='form__form-group-button']"

    # Login screen inputs
    _emailInput = "//input[@name='email']"
    _passwordInput = "//input[@name='password']"

    # Login screen messages
    _alertContent = "//div[@class='alert__content']"
    _emailAlertMessage = "//span[@class='form__form-group-error']"
    _passwordAlertMessage = "//span[contains(text(), 'A jelszónak 8 karakterből kell állnia, és tartalmaznia kell legalább 1 számjegyet, 1 nagybetűt és 1 kisbetűt.')]"

    ### Actions
    # Login
    def login(self, email, password):
        self.enterCredentials(email, password)
        self.elementClick(self._loginBtn)

    def enterCredentials(self, email, password):
        self.sendKeys(email, self._emailInput)
        self.sendKeys(password, self._passwordInput)

    def clickLoginBtn(self):
        self.elementClick(self._loginBtn)

    def clearCredentials(self):
        self.clearKeys(self._emailInput)
        self.clearKeys(self._passwordInput)

    def isLoginBtnVisible(self):
        isLoginBtnVisible = self.isElementPresent(self._loginBtn)
        return isLoginBtnVisible

    def alertContentCheck(self):
        isAlertContentVisible = self.isElementPresent(self._alertContent)
        return isAlertContentVisible

    def emptyFieldAlertMessageCheck(self):
        isEmailAlertMessageVisible = self.isElementPresent(self._emailAlertMessage)
        return isEmailAlertMessageVisible

    def passwordFormatAlertMessageCheck(self):
        ispasswordAlertMessageVisible = self.isElementPresent(self._passwordAlertMessage)
        return ispasswordAlertMessageVisible

    def clickPasswordVisibilityBtn(self):
        self.elementClick(self._passwordVisibilityBtn)

    # Registration
    def clickRegisterBtn(self):
        self.elementClick(self._registerBtn)
