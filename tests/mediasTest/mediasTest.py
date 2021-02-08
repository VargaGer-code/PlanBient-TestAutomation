from base.basepage import BasePage
from utilities.testStatus import TestStatus
from utilities.util import Util
from pages.loginPage.login_page import LoginPage
from pages.mediasPage.mediasPage import MediasPage
import utilities.custom_logger as cl
from ddt import ddt, data, unpack
from utilities.read_csv import getCSVData
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
        self.mediasPage = MediasPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.util = Util()
        self.testStatus = TestStatus(self.driver)

    @data(*getCSVData("mediasDatas.csv"))
    @unpack
    def test_addNewMedia(self, userEmailDDT, userpwDDT, mediaNameDDT, heightDDT, lenghtDDT, qtyDDT,
                              isDigitalDDT, detailsDDT, commentsDDT, contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.testStatus.mark(result=self.loginPage.checkLoginSuccessfull(), resultMessage="Login successfuly check")
        self.mediasPage.openMediasPage()
        self.testStatus.mark(result=self.mediasPage.checkMediaTitlePresent(), resultMessage="Open medias page check")
        self.mediasPage.openAddNewMedia()
        self.testStatus.mark(result=self.mediasPage.checkAddNewMediaTitlePresent(),
                             resultMessage="Open medias page check")
        self.mediasPage.fillNewMediaForm(mediaNameDDT, heightDDT, lenghtDDT, qtyDDT, detailsDDT, commentsDDT,
                                         contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT)
        self.mediasPage.clickSaveMediaBtn()
        self.testStatus.markFinal(testName="Media created successfully",
                                  result=self.mediasPage.checkMediaTitlePresent(),
                                  resultMessage="Open medias page check")


    @data(*getCSVData("mediasDatas.csv"))
    @unpack
    def validateNewMediaAdded(self, userEmailDDT, userpwDDT, mediaNameDDT, heightDDT, lenghtDDT, qtyDDT,
                              isDigitalDDT, detailsDDT, commentsDDT, contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.mediasPage.openMediasPage()
        mediaDatasFromTable = self.basePage.getParentRowElementsByChildFromTable(mediaNameDDT)
        mediaDatasFromFile = self.mediasPage.listFromTableData(mediaNameDDT, heightDDT, lenghtDDT, qtyDDT, isDigitalDDT)
        areListsMatch = self.util.verifyListMatch(mediaDatasFromFile, mediaDatasFromTable)
        assert areListsMatch == True
