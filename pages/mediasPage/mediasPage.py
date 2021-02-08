import utilities.custom_logger as cl
from base.basepage import BasePage
from pages.mainMenuPage.mainMenuPage import MainMenuPage as mainMenu
from utilities.util import Util
import logging


class MediasPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ### Medias page locators
    # Add new media
    _addNewMediaBtn = "//a[@href='/medias/create']"
    _mediaTitle = "//h3[contains(text(), 'Médiafelület lista')]"

    ### Add new media locators
    _addNewMediaTitle = "//h3[contains(text(), 'Médiafelület felvétel')]"
    # Common details
    _mediaNameField = "//input[@name='title']"
    _mediaTypeRadioBtn = ""
    _heightField = "//input[@name='height']"
    _lenghtField = "//input[@name='width']"
    _qtyField = "//input[@name='quantity']"
    _mediaDetailsField = "//textarea[@name='description']"
    _mediaCommentsField = "//textarea[@name='remarks']"

    # Marketing
    _targetGroupMultiSelect = ""
    _useProposalMultiSelect = ""
    _contactNumberField = "//input[@name='media_marketing.contacts']"
    _rentTimeDropDown = "//input[@class='autocomplete__input']"
    _customerCreativeRadioBtn = ""
    _extraOptionsMultiSelect = ""

    # Location details
    _postCodeField = "//input[@name='media_geodata.zip_code']"
    _cityField = "//input[@name='media_geodata.city']"
    _streetField = "//input[@name='media_geodata.street']"

    # Buttons
    _saveNewMediaBtn = "//button[@type='submit']"
    _cancelBtn = ""



    ### Actions
    # Medias list page

    def openMediasPage(self):
        self.elementClick(mainMenu._mediasMainBtn)
        self.elementClick(mainMenu._mediasListBtn)

    def openAddNewMedia(self):
        self.elementClick(self._addNewMediaBtn)

    def checkMediaTitlePresent(self):
        isMediaTitlePresent = self.isElementPresent(self._mediaTitle)
        return isMediaTitlePresent

    # Add new media page

    def checkAddNewMediaTitlePresent(self):
        isAddNewMediaTitlePresent = self.isElementPresent(self._addNewMediaTitle)
        return isAddNewMediaTitlePresent

    def fillNewMediaForm(self, mediaName, height, length, qty, details, comments, contactNum, rentTime, postCode, city, street):
        self.sendKeys(mediaName, self._mediaNameField)
        self.sendKeys(height, self._heightField)
        self.sendKeys(length, self._lenghtField)
        self.sendKeys(qty, self._qtyField)
        self.sendKeys(details, self._mediaDetailsField)
        self.sendKeys(comments, self._mediaCommentsField)
        self.sendKeys(contactNum, self._contactNumberField)
        self.sendKeys(rentTime, self._rentTimeDropDown)
        self.sendKeys(postCode, self._postCodeField)
        self.sendKeys(city, self._cityField)
        self.sendKeys(street, self._streetField)

    def clickSaveMediaBtn(self):
        self.elementClick(self._saveNewMediaBtn)

    def listFromTableData(self, mediaName, provider, length, height, qty, isDigital):
        listFromFileData = []
        listFromFileData.append(mediaName)
        listFromFileData.append(provider)
        listFromFileData.append(length)
        listFromFileData.append(height)
        listFromFileData.append(qty)
        listFromFileData.append(isDigital)
        self.log.info("listFromTableData is : " + str(listFromFileData))
        return listFromFileData

