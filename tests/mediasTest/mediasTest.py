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

    @data(*getCSVData(
        "C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\mediasTest\\mediasDatas.csv"))
    @unpack
    def fullmediatest(self, userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                    isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT,
                    customerCreativeDDT, extrasDDT,
                    contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        self.addNewMedia(userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                    isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT,
                    customerCreativeDDT, extrasDDT,
                    contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT)
        self.mediaViewDataVerification(userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                    isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT,
                    customerCreativeDDT, extrasDDT,
                    contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT)
        self.modifyMediaDataPageVerification(userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                                             isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT,
                                             customerCreativeDDT, extrasDDT,
                                             contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT)

    # @data(*getCSVData(
    #     "C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\mediasTest\\mediasDatas.csv"))
    # @unpack
    def addNewMedia(self, userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                    isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT,
                    customerCreativeDDT, extrasDDT,
                    contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        """
        Add new media, all fields are used. Datas are from mediasDatas.csv CSV file.
        """
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.testStatus.mark(result=self.mainMenu.isLoginSuccesfully(), resultMessage="Login successfuly check")
        self.mainMenu.openMediasTopbar()
        self.mainMenu.openMediasPage()
        self.testStatus.mark(result=self.mediasPage.checkMediaListPageTitlePresent(), resultMessage="Open medias page check")
        self.mediasPage.clickAddNewMedia()
        # self.testStatus.mark(result=self.mediasPage.checkAddNewMediaTitlePresent, resultMessage="Validate add new
        # media page opened")
        self.mediasPage.fillNewMediaForm(mediaName=mediaNameDDT, height=heightDDT, length=lenghtDDT, qty=qtyDDT,
                                         isDigital=isDigitalDDT, labels=labelsDDT, details=detailsDDT,
                                         comments=commentsDDT,
                                         targetGroup=targetGroupDDT, useProposal=useProposalDDT,
                                         customerCreative=customerCreativeDDT,
                                         extras=extrasDDT, contactNum=contactNumDDT, rentTime=rentTimeDDT,
                                         postCode=postCodeDDT, city=cityDDT, street=streetDDT)
        self.mediasPage.clickSaveMediaBtn()
        self.testStatus.mark(result=self.mediasPage.checkMediaListPageTitlePresent(),
                             resultMessage="Validate return to medias list page")
        self.testStatus.mark(result=self.mediasPage.isMediaNameInList(mediaName=mediaNameDDT),
                                  resultMessage="Add new media test")
        self.mainMenu.logout()
        self.testStatus.markFinal(testName="Add new media test",
                                  result=self.loginPage.isLoginBtnVisible(),
                                  resultMessage="Logout validate")

    # @data(*getCSVData(
    #     "C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\mediasTest\\mediasDatas.csv"))
    # @unpack
    def modifyMediaDataPageVerification(self, userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                                        isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT,
                                        customerCreativeDDT, extrasDDT,
                                        contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        """
        Open the given media's modification page. Then verify all the datas.
        """
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.mainMenu.openMediasTopbar()
        self.mainMenu.openMediasPage()
        self.mediasPage.clickModifyMediaBtn(mediaName=mediaNameDDT)
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._mediaNameField,
                            exceptedText=mediaNameDDT),
                            resultMessage="Verify media name")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._heightField,
                            exceptedText=heightDDT),
                            resultMessage="Verify height")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._lenghtField,
                            exceptedText=lenghtDDT),
                            resultMessage="Verify lenght")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._qtyField,
                            exceptedText=qtyDDT),
                            resultMessage="Verify quantity")
        self.testStatus.mark(self.mediasPage.verifyMultiselectData(
                            locatorName="Címkék",
                            exceptedText=labelsDDT),
                            resultMessage="Verify Címkék multiselect")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._mediaDetailsField,
                            exceptedText=detailsDDT),
                            resultMessage="Verify media details")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._mediaCommentsField,
                            exceptedText=commentsDDT),
                            resultMessage="Verify comments")
        self.testStatus.mark(self.mediasPage.verifyMultiselectData(
                            locatorName="Elérhető célcsoport",
                            exceptedText=targetGroupDDT),
                            resultMessage="Verify Elérhető célcsoport multiselect")
        self.testStatus.mark(self.mediasPage.verifyMultiselectData(
                            locatorName="Felhasználási javaslat",
                            exceptedText=useProposalDDT),
                            resultMessage="Verify Felhasználási javaslat multiselect")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._contactNumberField,
                            exceptedText=contactNumDDT),
                            resultMessage="Verify contact number")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._rentTimeDropDown,
                            exceptedText=rentTimeDDT),
                            resultMessage=" Bérlési időtartam egysége")
        self.testStatus.mark(self.mediasPage.verifyMultiselectData(
                            locatorName="Extra lehetőségek",
                            exceptedText=extrasDDT),
                            resultMessage="Verify Felhasználási javaslat multiselect")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._postCodeField,
                            exceptedText=postCodeDDT),
                            resultMessage="Verify postCode")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._cityField,
                            exceptedText=cityDDT),
                            resultMessage="Verify City")
        self.testStatus.mark(self.mediasPage.verifyInputFieldData(
                            locator=self.mediasPage._streetField,
                            exceptedText=streetDDT),
                            resultMessage="Verify street")
        self.mediasPage.clickSaveMediaBtn()
        self.testStatus.mark(result=self.mainMenu.isMediasPageOpenedSuccesfully(),
                                  resultMessage="Media list page opened")
        self.mainMenu.logout()
        self.testStatus.markFinal(testName="test_modify Media Data Verification",
                                  result=self.loginPage.isLoginBtnVisible(),
                                  resultMessage="is logout succesfull")

    @data(*getCSVData(
        "C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\mediasTest\\mediasDatas.csv"))
    @unpack
    def mediaViewDataVerification(self, userEmailDDT, userpwDDT, mediaNameDDT, lenghtDDT, heightDDT, qtyDDT,
                    isDigitalDDT, labelsDDT, detailsDDT, commentsDDT, targetGroupDDT, useProposalDDT,
                    customerCreativeDDT, extrasDDT,
                    contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT, streetDDT):
        """
        Validate datas in the medias view page.
        """
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.mainMenu.openMediasTopbar()
        self.mainMenu.openMediasPage()
        self.mediasPage.clickViewMediaBtn(mediaNameDDT)
        # Overall details
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._mediaTitleView,
                                                                   exceptedText=mediaNameDDT),
                             resultMessage="Verify media name in view")
        self.testStatus.mark(result=self.mediasPage.verifyMediaSizeView(heightDDT, lenghtDDT),
                             resultMessage="Verify media size in view")
        self.testStatus.mark(result=self.mediasPage.verifyQuantity(exceptedText=qtyDDT),
                             resultMessage="Verify media quantity in view")
        self.testStatus.mark(result=self.mediasPage.verifyRadioBtn(locator=self.mediasPage._mediaIsDigitalView,
                                                                   excepedOption=isDigitalDDT),
                             resultMessage="Verify isDigital in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._mediaDetailsView,
                                                                   exceptedText=detailsDDT),
                             resultMessage="Verify details in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._mediaCommentsView,
                                                                   exceptedText=commentsDDT),
                             resultMessage="Verify comments in view")
        # Marketing details
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._targetGroupView,
                                                                   exceptedText=targetGroupDDT),
                             resultMessage="Verify target group in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._useProposalView,
                                                                   exceptedText=useProposalDDT),
                             resultMessage="Verify use proposal in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._extraOptionsView,
                                                                   exceptedText=extrasDDT),
                             resultMessage="Verify extras in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._contactNumberView,
                                                                   exceptedText=contactNumDDT),
                             resultMessage="Verify contact number in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._rentTimeView,
                                                                   exceptedText=rentTimeDDT),
                             resultMessage="Verify rent time in view")
        self.testStatus.mark(result=self.mediasPage.verifyRadioBtn(locator=self.mediasPage._customerCreativeView,
                                                                   excepedOption=customerCreativeDDT),
                             resultMessage="Verify customer creative in view")
        # Location details
        self.mediasPage.clickLocationTab()
        self.mediasPage.webScrollToElement(self.mediasPage._viewBackBtn)
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._postCodeView,
                                                                   exceptedText=postCodeDDT),
                             resultMessage="Verify postCode in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._cityView,
                                                                   exceptedText=cityDDT),
                             resultMessage="Verify city in view")
        self.testStatus.mark(result=self.mediasPage.verifyViewText(locator=self.mediasPage._streetView,
                                                                   exceptedText=streetDDT),
                             resultMessage="Verify street in view")
        self.mediasPage.clickViewBackBtn()
        self.testStatus.mark(result=self.mediasPage.checkMediaListPageTitlePresent(),
                             resultMessage="Checking media page list title present")
        self.mainMenu.logout()
        self.testStatus.markFinal(testName="Verify media datas in view",
                                  result=self.loginPage.isLoginBtnVisible(),
                                  resultMessage="Checking logout succesful")

    @data(*getCSVData("C:\\Users\\Felhasználó\\PycharmProjects\\PlanBient-TestAutomation\\tests\\mediasTest\\mediasDatas.csv"))
    @unpack
    def validateNewMediaAdded(self, userEmailDDT, userpwDDT, mediaNameDDT, heightDDT, lenghtDDT, qtyDDT,
                              isDigitalDDT, detailsDDT, commentsDDT, contactNumDDT, rentTimeDDT, postCodeDDT, cityDDT,
                              streetDDT):
        self.loginPage.login(userEmailDDT, userpwDDT)
        self.mainMenu.openMediasPage()
        mediaDatasFromTable = self.basePage.getParentRowElementsByChildFromTable(mediaNameDDT)
        mediaDatasFromFile = self.mediasPage.listFromTableData(mediaNameDDT, heightDDT, lenghtDDT, qtyDDT, isDigitalDDT)
        areListsMatch = self.util.verifyListMatch(mediaDatasFromFile, mediaDatasFromTable)
        assert areListsMatch == True

    def test_multiselect(self):
        textList = ["new", "label", "fanta"]
        testString = "new-label-fanta"
        self.loginPage.login("gergo.varga+kozzetevo1@sensomedia.hu", "aaaaaaA1")
        self.mainMenu.openMediasTopbar()
        self.mainMenu.openMediasPage()
        self.mediasPage.clickAddNewMedia()
        self.mediasPage.addValuesToMultiSelectField(self.mediasPage._labelsMultiSelect, testString)
        self.mediasPage.compareMultiselectValues(actualValues=self.mediasPage.getElementsTextFromMultiselectField(locator="Címkék"),
                                                 exceptedValues=textList)
        self.mediasPage.isMultiselectElementVisible(multiSelectName="Címkék", multiSelectElement="fanta")
        # self.mediasPage.clickOnSpecificMultiselectValue(locator="Címkék", valueToClick="fanta")
        self.mediasPage.clickOnAllMultiselectValue("Címkék")
        self.mediasPage.isMultiselectElementVisible(multiSelectName="Címkék", multiSelectElement="fanta")









