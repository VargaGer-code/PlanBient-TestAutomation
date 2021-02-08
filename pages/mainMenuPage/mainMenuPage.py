import utilities.custom_logger as cl
from base.basepage import BasePage
from utilities.util import Util
import logging

class MainMenuPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ### Main menu locators


    ### Médiafelületek kezelése
    _mediasMainBtn = "//button[contains(text(),'Médiafelületek kezelése')]"
    # Médiafelületek listája
    _mediasListBtn = "//p[contains(text(),'Médiafelületek listája')]"

    ### Beállítások és opciók
    # Beállítások és opciók nagy gomb
    _settingsAndOptionsBtn = "//button[contains(text(),'Beállítások és opciók')]"

    ### User profile and other stuff
    _userSettingsBtn = "//div[@class='topbar__right']//button[1]"
    _logoutBtn = "//p[contains(text(),'Kilépés')]"
    # User profile
    _profileBtn = "//a[@href='/profile']"
    _userProfileType = "//p[contains(text(),'Jogosultsági szint')]//parent::div//span[contains(text(),'Közzétevő')]"
    _userProfileHeaderText = "//h3[contains(text(),'Felhasználói profil')]"

    ### Actions
    # User profile and other stuff
    def openSettingsTopbar(self):
        self.waitForElement(self._userSettingsBtn)
        self.mouseHover(self._userSettingsBtn)

    def openUserProfile(self):
        self.elementClick(self._profileBtn)

    def isProfileOpenedSuccesfully(self):
        isUserProfileOpened = self.isElementPresent(self._userProfileHeaderText)
        return isUserProfileOpened

    def logout(self):
        self.openSettingsTopbar()
        self.elementClick(self._logoutBtn)

    def checkUserName(self, userName):
        if self.isElementNotDisplayed("//p[contains(text(),'Felhasználói név')]//parent::div//span[contains(text(),'" + userName + "')]") == True:
            return False
        else:
            isUserNameMatch = self.isElementPresent("//p[contains(text(),'Felhasználói név')]//parent::div//span[contains(text(),'" + userName + "')]")
        return isUserNameMatch

    def checkUserType(self, userType):
        if self.isElementNotDisplayed("//p[contains(text(),'Jogosultsági szint')]//parent::div//span[contains(text(),'" + userType + "')]") == True:
            return False
        else:
            isUserProfileMatch = self.isElementPresent("//p[contains(text(),'Jogosultsági szint')]//parent::div//span[contains(text(),'" + userType + "')]")
        return isUserProfileMatch