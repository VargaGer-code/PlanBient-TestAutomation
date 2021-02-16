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

    ### Topbar menu locators

    ### Médiafelületek kezelése
    _mediasMainBtn = "//button[contains(text(),'Médiafelületek kezelése')]"
    # Médiafelületek listája oldal
    _mediasPageBtn = "//a[@href='/medias']"
    # Médiafelületek lista title
    _mediasPageTitle = "//h3[contains(text(),'Médiafelület lista')]"

    ### Projektek és folyamatok
    _projectsMainBtn = "//button[contains(text(),'Projektek és folyamatok')]"

    # Kampányok kezelése
    _campaignsPageBtn = "//a[@href='/campaigns']"
    # Kampányok lista title
    _campaignsPageTitle = "//h3[contains(text(),'Kampányok lista')]"

    ### Beállítások és opciók
    _settingsAndOptionsBtn = "//button[contains(text(),'Beállítások és opciók')]"

    # Munkatársak
    _employeesPageBtn = "//a[@href='/employees']"
    _employeesPageTitle = "//h3[contains(text(),'Munkatársak lista')]"
    # Partnerek
    _partnersPageBtn = "//a[@href='/partners']"
    _partnersPageTitle = "//h3[contains(text(),'Partner lista')]"
    # Felhasználók
    _usersPageBtn = "//a[@href='/accounts']"
    _usersPageTitle = "//h3[contains(text(),'Felhasználó lista')]"

    ### User profile and other stuff
    _userSettingsBtn = "//div[@class='topbar__right']//button[1]"
    _logoutBtn = "//p[contains(text(),'Kilépés')]"
    # User profile
    _profilePageBtn = "//a[@href='/profile']"
    _userProfileType = "//p[contains(text(),'Jogosultsági szint')]//parent::div//span[contains(text(),'Közzétevő')]"
    _userProfileHeaderText = "//h3[contains(text(),'Felhasználói profil')]"

    ### Actions
    def isLoginSuccesfully(self):
        isLoginSuccesfully = self.isElementPresent(self._settingsAndOptionsBtn)
        return isLoginSuccesfully

    ### Media operations
    def isMediasTopbarVisible(self):
        isMediasTopbarVisible = self.isElementPresent(self._mediasMainBtn)
        return isMediasTopbarVisible

    def openMediasTopbar(self):
        self.waitForElement(self._mediasMainBtn, timeout=3)
        self.mouseHover(self._mediasMainBtn)

        # Medias
    def isMediasPageBtnVisible(self):
        isMediasPageBtnVisible = self.isElementPresent(self._mediasPageBtn)
        return isMediasPageBtnVisible

    def openMediasPage(self):
        self.elementClick(self._mediasPageBtn)

    def isMediasPageOpenedSuccesfully(self):
        isMediasPageOpenedSuccesfully = self.isElementPresent(self._mediasPageTitle)
        return isMediasPageOpenedSuccesfully

    ### Projects
    def isProjectTopbarVisible(self):
        isProjectTopbarVisible = self.isElementPresent(self._projectsMainBtn)
        return isProjectTopbarVisible

    def openProjectTopbar(self):
        self.waitForElement(self._projectsMainBtn, timeout=3)
        self.mouseHover(self._projectsMainBtn)

        # Campaigns
    def isCampaignPageBtnVisible(self):
        isCampaignPageBtnVisible = self.isElementPresent(self._campaignsPageBtn)
        return isCampaignPageBtnVisible

    def openCampaignPage(self):
        self.openProjectTopbar()
        self.elementClick(self._campaignsPageBtn)

    def isCampaignPageOpenedSuccesfully(self):
        isCampaignPageOpenedSuccesfully = self.isElementPresent(self._campaignsPageTitle)
        return isCampaignPageOpenedSuccesfully

    ### Settings and options
    def isSettingsAndOptionsTopbarVisible(self):
        isSettingsAndOptionsTopbarVisible = self.isElementPresent(self._settingsAndOptionsBtn)
        return isSettingsAndOptionsTopbarVisible

    def openSettingsAndOptionsTopbar(self):
        self.waitForElement(self._settingsAndOptionsBtn)
        self.mouseHover(self._settingsAndOptionsBtn)

        # Employees
    def isEmployeesPageBtnVisible(self):
        isEmployeesPageBtnVisible = self.isElementPresent(self._employeesPageBtn)
        return isEmployeesPageBtnVisible

    def openEmployeesPage(self):
        self.openSettingsAndOptionsTopbar()
        self.elementClick(self._employeesPageBtn)

    def isEmployeesPageOpenedSuccesfully(self):
        isEmployeesPageOpenedSuccesfully = self.isElementPresent(self._employeesPageTitle)
        return isEmployeesPageOpenedSuccesfully

        # Partners
    def isPartnersPageBtnVisible(self):
        isPartnersPageBtnVisible = self.isElementPresent(self._partnersPageBtn)
        return isPartnersPageBtnVisible

    def openPartnersPage(self):
        self.openSettingsAndOptionsTopbar()
        self.elementClick(self._partnersPageBtn)

    def isPartnersPageOpenedSuccesfully(self):
        isPartnersPageOpenedSuccesfully = self.isElementPresent(self._partnersPageTitle)
        return isPartnersPageOpenedSuccesfully

        # Users
    def isUsersPageBtnVisible(self):
        isUsersPageBtnVisible = self.isElementPresent(self._usersPageBtn)
        return isUsersPageBtnVisible

    def openUsersPage(self):
        self.openSettingsAndOptionsTopbar()
        self.elementClick(self._usersPageBtn)

    def isUsersPageOpenedSuccesfully(self):
        isUsersPageOpenedSuccesfully = self.isElementPresent(self._usersPageTitle)
        return isUsersPageOpenedSuccesfully

    # User profile settings, logout and other stuff
    def isSettingsTopbarVisible(self):
        isSettingsTopbarVisible = self.isElementPresent(self._userSettingsBtn)
        return isSettingsTopbarVisible

    def openSettingsTopbar(self):
        self.waitForElement(self._userSettingsBtn)
        self.mouseHover(self._userSettingsBtn)

        # User profile page
    def openUserProfile(self):
        self.elementClick(self._profilePageBtn)

    def isProfileOpenedSuccesfully(self):
        """
        Validates user profile is opened by header text
        """
        isUserProfileOpened = self.isElementPresent(self._userProfileHeaderText)
        return isUserProfileOpened

    def checkUserName(self, userName):
        """
        Validates userName displayed in user profile menu.
        :param userName: Username to validate
        :return: False if username is NOT displayed ; True if username is displayed
        """
        if self.isElementNotDisplayed("//p[contains(text(),'Felhasználói név')]//parent::div//span[contains(text(),'" + userName + "')]") == True:
            return False
        else:
            isUserNameMatch = self.isElementPresent("//p[contains(text(),'Felhasználói név')]//parent::div//span[contains(text(),'" + userName + "')]")
        return isUserNameMatch

    def checkUserType(self, userType):
        """
        Validates userType displayed in user profile menu.
        :param userName: userType to validate (Admin, Reklámközzétevő, MHFÉ, Reklámközvetítő, Reklámozó)
        :return: False if userType is NOT displayed ; True if userType is displayed
        """
        if self.isElementNotDisplayed("//p[contains(text(),'Jogosultsági szint')]//parent::div//span[contains(text(),'" + userType + "')]") == True:
            return False
        else:
            isUserProfileMatch = self.isElementPresent("//p[contains(text(),'Jogosultsági szint')]//parent::div//span[contains(text(),'" + userType + "')]")
        return isUserProfileMatch

        # Logout
    def logout(self):
        self.openSettingsTopbar()
        self.elementClick(self._logoutBtn)