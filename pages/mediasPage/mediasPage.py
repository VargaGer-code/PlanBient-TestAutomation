import utilities.custom_logger as cl
from base.basepage import BasePage
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
    _addNewMediaBtn = "Új médiafelület"
    _mediaTitle = "//h3[contains(text(), 'Médiafelület lista')]"

    ### Add new media locators
    _addNewMediaTitle = "//h3[contains(text(), 'Médiafelület felvétel')]"
    # Common details
    _mediaNameField = "//input[@name='title']"
    _mediaTypeRadioBtn = "//span[contains(text(), 'Digitális')]//parent::div//div[@class='form__form-group-field']//label[@class='radio-btn']"
    _labelsMultiSelect = "//span[contains(text(), 'Címkék')]//parent::div//input[@class='multiple-search-select__input']"
    _heightField = "//input[@name='height']"
    _lenghtField = "//input[@name='width']"
    _qtyField = "//input[@name='quantity']"
    _mediaDetailsField = "//textarea[@name='description']"
    _mediaCommentsField = "//textarea[@name='publisher_notes']"

    # Marketing
    _targetGroupMultiSelect = "//span[contains(text(), 'Elérhető')]//parent::div//input[@class='multiple-search-select__input']"
    _useProposalMultiSelect = "//span[contains(text(), 'Felhasználás')]//parent::div//input[@class='multiple-search-select__input']"
    _contactNumberField = "//input[@name='media_marketing.contacts']"
    _rentTimeDropDown = "//input[@class='autocomplete__input']"
    _customerCreativeRadioBtn = "//span[contains(text(), 'Ügyfél')]//parent::div//div[@class='form__form-group-field']//label[@class='radio-btn']"
    _extraOptionsMultiSelect = "//span[contains(text(), 'Extra')]//parent::div//input[@class='multiple-search-select__input']"

    # Location details
    _postCodeField = "//input[@name='media_geodata.zip_code']"
    _cityField = "//input[@name='media_geodata.city']"
    _streetField = "//input[@name='media_geodata.street']"

    # Buttons
    _saveNewMediaBtn = "//button[@type='submit']"
    _cancelBtn = "//button[contains(text(), 'Mégse')]"



    ### Actions
    # Medias list page

    def openAddNewMedia(self):
        self.elementClick(self._addNewMediaBtn, "link")

    def checkMediaTitlePresent(self):
        isMediaTitlePresent = self.isElementPresent(self._mediaTitle)
        return isMediaTitlePresent

    def isMediaNameInList(self, mediaName):
        """
        Checking if media's name is in the medias list
        :return: True if its visible in list, False if its not
        """
        isMediaNameInList = self.isElementPresent("//td[contains(text(), '" + mediaName + "')]")
        return isMediaNameInList


    # Add new media page

    def checkAddNewMediaTitlePresent(self):
        isAddNewMediaTitlePresent = self.isElementPresent(self._addNewMediaTitle)
        return isAddNewMediaTitlePresent

    def fillNewMediaForm(self, mediaName, height, length, qty, isDigital, labels, details, comments, targetGroup,
                         useProposal, customerCreative, extras, contactNum, rentTime, postCode, city, street):
        # Common details
        self.sendKeys(mediaName, self._mediaNameField)
        self.sendKeys(length, self._lenghtField)
        self.sendKeys(height, self._heightField)
        self.sendKeys(qty, self._qtyField)
        if isDigital == "1":
            self.elementClick(self._mediaTypeRadioBtn + "[1]")
        elif isDigital == "2":
            self.elementClick(self._mediaTypeRadioBtn + "[2]")
        self.sendKeysWithEnter(labels, self._labelsMultiSelect)
        self.sendKeys(details, self._mediaDetailsField)
        self.sendKeys(comments, self._mediaCommentsField)
        # Marketing
        self.webScrollToElement(self._saveNewMediaBtn)
        self.sendKeysWithEnter(targetGroup, self._targetGroupMultiSelect)
        self.sendKeysWithEnter(useProposal, self._useProposalMultiSelect)
        #self.clickNearElement(self._customerCreativeRadioBtn, xOffset=-400)
        self.sendKeys(contactNum, self._contactNumberField)
        self.sendKeys(rentTime, self._rentTimeDropDown)
        if customerCreative == "1":
            self.elementClick(self._customerCreativeRadioBtn + "[1]")
        if customerCreative == "2":
            self.elementClick(self._customerCreativeRadioBtn + "[2]")
        self.sendKeysWithEnter(extras, self._extraOptionsMultiSelect)
        # Location details
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

