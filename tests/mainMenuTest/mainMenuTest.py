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
    def validateUserProfiles(self, emailDDT, pwDDT, userNameDDT, userTypeDDT, mediasMainBtnDDT, mediasPageDDT,
                             projectsMainBtnDDT, campaignPageDDT, settingsMainBtnDDT, ColleguesDDT, PartnersDDT, users):
        """
        Validates user datas in profile menu
        """
        self.loginPage.login(emailDDT, pwDDT)
        self.testStatus.mark(self.loginPage.checkLoginSuccessfull(), "Login successful validation")
        self.mainMenu.openSettingsTopbar()
        self.mainMenu.openUserProfile()
        self.testStatus.mark(self.mainMenu.isProfileOpenedSuccesfully(), resultMessage="Profile page validation")
        self.testStatus.mark(self.mainMenu.checkUserName(userNameDDT), resultMessage="Username validation")
        self.testStatus.mark(self.mainMenu.checkUserType(userTypeDDT), resultMessage="User Type Validation")
        self.mainMenu.logout()
        self.testStatus.markFinal("User profile validation", result=self.loginPage.isLoginBtnVisible(), resultMessage="Login page validation failed")

    @data(*getCSVData("tests/mainMenuTest/mainMenus.csv"))
    @unpack
    def test_validateMenus(self, emailDDT, pwDDT, userNameDDT, userTypeDDT, mediasMainBtnDDT, mediasPageDDT,
                             projectsMainBtnDDT, campaignPageDDT, settingsMainBtnDDT, colleguesDDT, partnersDDT, users):
        """
        1 : Validate if menu is visible
        0 : Validate if menu is NOT visible
        """
        self.loginPage.login(emailDDT, pwDDT)
        # Validate media menus
        if mediasMainBtnDDT == "1":
            self.testStatus.mark(result=self.mainMenu.isMediasTopbarVisible(),
                                 resultMessage="MediasMainBtn visibility")
            self.mainMenu.openMediasTopbar()
            # validate medias list menu
            if mediasPageDDT == "1":
                self.testStatus.mark(result=self.mainMenu.isMediasPageBtnVisible(),
                                     resultMessage="MediasPageBtn visibility")
                self.mainMenu.openMediasPage()
                self.testStatus.mark(resultMessage="Medias page open validate",
                                     result=self.mainMenu.isMediasPageOpenedSuccesfully())
            elif mediasPageDDT == "0":
                self.testStatus.mark(result=not self.mainMenu.isMediasPageBtnVisible(),
                                     resultMessage="MediasPageBtn visibility")
        elif mediasMainBtnDDT == "0":
            self.testStatus.mark(result=not self.mainMenu.isMediasTopbarVisible(),
                                      resultMessage="MediasMainBtn visibility")
        # Validate project menus
        if projectsMainBtnDDT == "1":
            self.testStatus.mark(result=self.mainMenu.isProjectTopbarVisible(),
                                 resultMessage="Project Topbar visibility")
            self.mainMenu.openProjectTopbar()
            # Validate campaign menu
            if campaignPageDDT == "1":
                self.testStatus.mark(result=self.mainMenu.isCampaignPageBtnVisible(),
                                     resultMessage="Campaign btn visibility")
                self.mainMenu.openCampaignPage()
                self.testStatus.mark(resultMessage="Campaign page open validate",
                                     result=self.mainMenu.isCampaignPageOpenedSuccesfully())
            elif campaignPageDDT == "0":
                self.testStatus.mark(result=not self.mainMenu.isCampaignPageBtnVisible(),
                                     resultMessage="Campaign btn visibility")
        elif projectsMainBtnDDT == "0":
            self.testStatus.mark(result= not self.mainMenu.isProjectTopbarVisible(),
                                 resultMessage="Project Topbar visibility")
        # validate Options menu
        if settingsMainBtnDDT == "1":
            self.testStatus.mark(result=self.mainMenu.isSettingsAndOptionsTopbarVisible(),
                                 resultMessage="Settings and options Topbar visibility")
            self.mainMenu.openSettingsAndOptionsTopbar()
            # Validate employees menu
            if colleguesDDT == "1":
                self.testStatus.mark(result=self.mainMenu.isEmployeesPageBtnVisible(),
                                     resultMessage="Employee btn visibility")
                self.mainMenu.openEmployeesPage()
                self.testStatus.mark(resultMessage="Employee page open validate",
                                     result=self.mainMenu.isEmployeesPageOpenedSuccesfully())
            elif campaignPageDDT == "0":
                self.testStatus.mark(result=not self.mainMenu.isEmployeesPageBtnVisible(),
                                     resultMessage="Employee btn visibility")
            # Validate partners menu
            if partnersDDT == "1":
                self.testStatus.mark(result=self.mainMenu.isPartnersPageBtnVisible(),
                                     resultMessage="Partners btn visibility")
                self.mainMenu.openPartnersPage()
                self.testStatus.mark(resultMessage="Partner page open validate",
                                     result=self.mainMenu.isPartnersPageOpenedSuccesfully())
            elif partnersDDT == "0":
                self.testStatus.mark(result=not self.mainMenu.isPartnersPageBtnVisible(),
                                     resultMessage="Partners btn visibility")
            # Users
            if users == "1":
                self.testStatus.mark(result=self.mainMenu.isUsersPageBtnVisible(),
                                     resultMessage="Users btn visibility")
                self.mainMenu.openUsersPage()
                self.testStatus.mark(resultMessage="Users page open validate",
                                     result=self.mainMenu.isUsersPageOpenedSuccesfully())
            elif users == "0":
                self.testStatus.mark(result=not self.mainMenu.isUsersPageBtnVisible(),
                                     resultMessage="Users btn visibility")
        self.mainMenu.logout()
        self.testStatus.markFinal(testName="MediasMainBtn",
                                  result=self.loginPage.isLoginBtnVisible(),
                                  resultMessage="MediasMainBtn")
