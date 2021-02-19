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

    ### Add new / modify media locators
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

    ### View media datasheet locators
    _mediaTitleView = "//h4[@class='media-card__title']"
    _mediaSizeView = "//p[contains(text(), 'Méret')]//parent::div//span"
    _mediaQuantityView = "//p[contains(text(), 'Darabszám')]//parent::div//span"
    _mediaIsDigitalView = "//p[contains(text(), 'Digitális felület')]//parent::div//span"
    _mediaDetailsView = "//p[contains(text(), 'Leírás')]//parent::div//div"
    _mediaCommentsView = "//p[contains(text(), 'Reklámközzétevő feljegyzései')]//parent::div//div"

    # View Marketing datas
    _marketingTab = "//a[contains(text(),'Marketing adatok')]"
    _targetGroupView = "//p[contains(text(), 'Elérhető célcsoport')]//parent::div//span"
    _useProposalView = "//p[contains(text(), 'Felhasználási javaslat')]//parent::div//span"
    _contactNumberView = "//p[contains(text(), 'Kontaktusszám')]//parent::div//span"
    _rentTimeView = "//p[contains(text(), 'Bérlési időtartam egysége')]//parent::div//span"
    _customerCreativeView = "//p[contains(text(), 'Ügyfél gyárthatja-e a kreatívot?')]//parent::div//span"
    _extraOptionsView = "//p[contains(text(), 'Extra lehetőségek')]//parent::div//span"

    # View Location datas
    _locationTab = "//a[contains(text(),'Helyszín')]"
    _postCodeView = "//p[contains(text(), 'Irányítószám')]//parent::div//span"
    _cityView = "//p[contains(text(), 'Település')]//parent::div//span"
    _streetView = "//p[contains(text(), 'Közterület adatai')]//parent::div//span"

    # View Other datas
    _otherTab = "//a[contains(text(),'Egyéb adatok')]"

    _viewBackBtn = "//button[contains(text(),'Vissza')]"

    ### Actions
    # Medias list page

    def clickAddNewMedia(self):
        self.elementClick(self._addNewMediaBtn, "link")

    def clickModifyMediaBtn(self, mediaName):
        self.elementClick("//td[contains(text(),'" + mediaName + "')]//parent::tr//a[@title='Szerkesztés']")

    def clickViewMediaBtn(self, mediaName):
        self.elementClick("//td[contains(text(),'" + mediaName + "')]//parent::tr//a[@title='Adatlap']")

    def checkMediaListPageTitlePresent(self):
        isMediaTitlePresent = self.isElementPresent(self._mediaTitle)
        return isMediaTitlePresent

    def isMediaNameInList(self, mediaName):
        """
        Checking if media's name is in the medias list
        :return: True if its visible in list, False if its not
        """
        isMediaNameInList = self.isElementPresent("//td[contains(text(), '" + mediaName + "')]")
        return isMediaNameInList

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
        #  1 - igen , 2 - Nem
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
        # self.clickNearElement(self._customerCreativeRadioBtn, xOffset=-400)
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

    # Multiselect functions
    def addValuesToMultiSelectField(self, locator, dataString, locatorType="xpath"):
        """
        Send datas to multiselect. Put an enter after each value
        :param locator: multiselect locator
        :param listOfValues: strings to put into multiselect input
        """
        list = dataString.split("-")
        for value in range(len(list)):
            self.sendKeysWithEnter(data=list[value], locator=locator, locatorType=locatorType)

    def getElementsTextFromMultiselectField(self, locator):
        """
        Get the text from multiselect values.
        :param locator: Multiselect locator
        :return: List with the multiselect values
        """
        elementList = self.getTexts("//span[contains(text(), '" + locator + "')]//parent::div//div[@class='form__form-group-input-wrap']//div[@class='multiple-search-select__label']")
        return elementList

    def compareMultiselectValues(self, actualValues, exceptedValues):
        """
        Compare the multiselect values with the given excepted values.
        :return: True if lists are match, False if not match
        """
        areListsMatch = self.util.verifyListMatch(expectedList=exceptedValues, actualList=actualValues)
        return areListsMatch

    def clickOnSpecificMultiselectValue(self, locator, valueToClick):
        """
        Clicks on a specific multiselect value
        valueToClick: String, clicking on this web element
        """
        self.elementClick("//span[contains(text(), '" + locator + "')]//parent::div//div[@class='form__form-group-input-wrap']//div[contains(text(),'" + valueToClick + "')]")

    def clickOnAllMultiselectValue(self, locator):
        """
        Clicks on all the elements in a multiSelect field
        :param locator: Multiselect field name
        """
        elementList = self.getTexts("//span[contains(text(), '" + locator + "')]//parent::div//div[@class='form__form-group-input-wrap']//div[@class='multiple-search-select__label']")
        for element in range(len(elementList)):
            self.elementClick("//span[contains(text(), '" + locator + "')]//parent::div//div[@class='form__form-group-input-wrap']//div[contains(text(),'" + elementList[element] + "')]")

    def isMultiselectElementVisible(self, multiSelectName, multiSelectElement):
        """
        Check if element is visible in multiselect field
        :param multiSelectName: Multiselect field name
        :param multiSelectElement: Element to validate visibility
        :return: True if visible, False if not visible
        """
        isElementVisible = self.isElementPresent("//span[contains(text(), '" + multiSelectName +
                                                 "')]//parent::div//div[@class='form__form-group-input-wrap']//div[contains(text(),'" + multiSelectElement + "')]")
        return isElementVisible

    #def clickOnAllMultiselectValue(self):

    def clickSaveMediaBtn(self):
        self.elementClick(self._saveNewMediaBtn)

    # Modify media page
    def verifyInputFieldData(self, locator, exceptedText):
        result = self.util.verifyTextMatch(actualText=BasePage.getTextFromInputField(self, locator),
                                           expectedText=exceptedText)
        return result

    def verifyMultiselectData(self, locatorName, exceptedText):
        result = self.util.verifyTextMatch(actualText=BasePage.getTextFromMultiSelectField(self, locatorName),
                                           expectedText=exceptedText)
        return result

    # View media page
    def clickMarketingTab(self):
        self.elementClick(self._marketingTab)

    def clickLocationTab(self):
        self.elementClick(self._locationTab)

    def clickOtherTab(self):
        self.elementClick(self._otherTab)

    def clickViewBackBtn(self):
        self.elementClick(self._viewBackBtn)

    def verifyViewText(self, locator, exceptedText):
        result = self.verifyText(actualText=locator,
                                 exceptedText=exceptedText)
        return result

    def formatMediaSize(self, height, length, unit="cm"):
        formattedSize = height + " x " + length + " " + unit
        return formattedSize

    def verifyMediaSizeView(self, height, length):
        result = self.verifyText(actualText=self._mediaSizeView,
                                 exceptedText=self.formatMediaSize(height=height, length=length))
        return result

    def formatQuantity(self, quantity):
        formattedQty = quantity + " db"
        return formattedQty

    def verifyQuantity(self, exceptedText):
        result = self.verifyText(actualText=self._mediaQuantityView,
                                 exceptedText=self.formatQuantity(exceptedText))
        return result

    def formatRadioBtntoText(self, text):
        if text == "Igen":
            return "1"
        elif text == "Nem":
            return "2"

    def verifyRadioBtn(self, locator, excepedOption):
        optionText = self.getText(locator)
        radioBtnOption = self.formatRadioBtntoText(optionText)
        if excepedOption == radioBtnOption:
            return True
        elif excepedOption != radioBtnOption:
            return False