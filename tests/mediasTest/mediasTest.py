from base.basepage import BasePage
from utilities.testStatus import TestStatus
from utilities.util import Util
from pages.loginPage.login_page import LoginPage
from pages.mediasPage.mediasPage import MediasPage
from pages.mainMenuPage.mainMenuPage import MainMenuPage
import utilities.custom_logger as cl
from ddt import ddt, data, unpack
from utilities.read_csv import getCSVData
import unittest
import pytest
import logging

# pytest tests\mediasTest\mediasTest.py -s -v --browser edge

@ddt
@pytest.mark.usefixtures("getWebdriver")
class MediasTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, getWebdriver):
        log = cl.customLogger(logging.DEBUG)
        self.loginPage = LoginPage(self.driver)
        self.mediasPage = MediasPage(self.driver)
        self.mainMenu = MainMenuPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.util = Util()
        self.testStatus = TestStatus(self.driver)

    @data(*getCSVData("C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\mediasTest\\mediasDatas.csv"))
    @unpack
    def test_addNewMedia(self, userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                              isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT, customerCreativeDDT, extrasDDT,
                            contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.testStatus.mark(result=self.mainMenu.isLoginSuccesfully(), resultMessage="Login successfuly check")
        self.mainMenu.openMediasTopbar()
        self.mainMenu.openMediasPage()
        self.testStatus.mark(result=self.mediasPage.checkMediaTitlePresent(), resultMessage="Open medias page check")
        self.mediasPage.openAddNewMedia()
        #self.testStatus.mark(result=self.mediasPage.checkAddNewMediaTitlePresent, resultMessage="Validate add new media page opened")
        self.mediasPage.fillNewMediaForm(mediaName=mediaNameDDT, height=heightDDT, length=lenghtDDT, qty=qtyDDT,
                            isDigital=isDigitalDDT, labels=labelsDDT, details=detailsDDT, comments=commentsDDT,
                            targetGroup=targetGroupDDT, useProposal=useProposalDDT, customerCreative=customerCreativeDDT,
                            extras=extrasDDT, contactNum=contactNumDDT, rentTime=rentTimeDDT, postCode=postCodeDDT, city=cityDDT, street=streetDDT)
        self.mediasPage.clickSaveMediaBtn()
        self.testStatus.mark(result=self.mediasPage.checkMediaTitlePresent(), resultMessage="Validate return to medias list page")
        self.testStatus.markFinal(testName="Add new media test", result=self.mediasPage.isMediaNameInList(mediaName=mediaNameDDT),
                                  resultMessage="Add new media test")


    @data(*getCSVData("C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\mediasTest\\mediasDatas.csv"))
    @unpack
    def validateNewMediaAdded(self, userEmailDDT, userpwDDT, mediaNameDDT, heightDDT, lenghtDDT, qtyDDT,
                              isDigitalDDT, detailsDDT, commentsDDT, contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.mainMenu.openMediasPage()
        mediaDatasFromTable = self.basePage.getParentRowElementsByChildFromTable(mediaNameDDT)
        mediaDatasFromFile = self.mediasPage.listFromTableData(mediaNameDDT, heightDDT, lenghtDDT, qtyDDT, isDigitalDDT)
        areListsMatch = self.util.verifyListMatch(mediaDatasFromFile, mediaDatasFromTable)
        assert areListsMatch == True
