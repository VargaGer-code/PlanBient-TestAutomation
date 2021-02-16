from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utilities.util import Util
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDrivers():
    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        self.driver = driver
        self.util = Util()

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current page:
        """
        filename = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenShotDir = "../screenshots/"
        # Mindig a jelenlegi mappából számol
        relativeFileName = screenShotDir + filename
        # Get the directory name of the current file
        currentDir = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDir, relativeFileName)
        destinationDir = os.path.join(currentDir, screenShotDir)

        try:
            # Check if destinationDir is exist
            if not os.path.exists(destinationDir):
                # Ha nincs ilyen mappa, létrehozza
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Screenshot error Occured")
            #print_stack()

    def getElementList(self, locator, locatorType="xpath"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element


    def getByType(self, locatorType="xpath"):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locator type: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="xpath", clickNumber=1, secBetweenClicks=0, element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # locator is not empty
                element = self.getElement(locator, locatorType)
            for i in range(clickNumber):
                element.click()
                self.util.sleep(secBetweenClicks)
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            #print_stack()
            self.screenShot(locator + " not found")
            assert False

    def clickNearElement(self, locator="", xOffset=0, yOffset=0, locatorType="xpath"):
        """
        Click near an element
        """
        try:
            element = self.getElement(locator, locatorType)
            ActionChains(self.driver).move_to_element(to_element=element).move_by_offset(xoffset=xOffset, yoffset=yOffset).click_and_hold().release().perform()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            self.screenShot(locator + " not found")
            assert False



    def sendKeys(self, data, locator="", locatorType="xpath", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            #print_stack()

    def sendKeysWithEnter(self, data, locator="", locatorType="xpath", element=None):
        """
        Send keys to an element then press enter at the end
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            element.send_keys(Keys.ENTER)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            #print_stack()


    def getText(self, locator="", locatorType="xpath", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # Locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            #print_stack()
            text = None
        return text


    def getTexts(self, locator="", locatorType="xpath", element=None):
        textList = []
        """
        Get 'Texts' from elements, and put the elements into a list
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # Locator is not empty
                element = self.getElementList(locator, locatorType)
                self.log.debug("Element length: " + str(len(element)))
            for elements in element:
                textList.append(self.getText(elements))
                self.log.debug("Text on element: " + str(self.getText(elements)))
        except:
            self.log.error("Failed to get text on element")
            #print_stack()
        return textList


    def clearKeys(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
        except:
            self.log.info("Cannot clear data on the element: " + locator + " LocatorType: " + locatorType)


    def isElementPresent(self, locator="", locatorType="xpath", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="xpath", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def isElementNotDisplayed(self, element, locatorType="xpath"):
        """
        :param element: Element to check
        :param locatorType: Locatory type, default xpath
        :return: True if element is NOT displayed, False if element is displayed
        """
        isElementDisplayed = self.getElementList(element, locatorType)
        self.log.info("Element length (0 if NOT displayed) :: " + str(len(isElementDisplayed)))
        if len(isElementDisplayed) == 0:
            return True
        else:
            return False

    def waitUntilElementIsDisplayed(self, locator, locatorType="xpath", timeout=10, pollFrequency=0.5):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotSelectableException])
            element = self.getElement(locator, locatorType="xpath")
            displayedElement = wait.until(EC.visibility_of_element_located(element))
            self.log.info("Element " + locator + " is displayed")
            return displayedElement

        except:
            self.log.info("Element not found")

    def elementPresenceCheck(self, locator, byType="xpath"):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element presence is Found with locator: " + locator + "with type: " + byType)
                return True
            else:
                self.log.info("Element not found with locator: " + locator + "with type: " + byType)
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="xpath",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element " + locator + " appeared on the web page")
        except:
            self.log.info("Element " + locator + " not appeared on the web page")
            #print_stack()
        return element

    def isElementEnabled(self, locator, locatorType="xpath"):
        """
        Megnézi egy elem-ben van-e 'disabled' parameter
        :param locator:
        :param locatorType:
        :return: Boolean
        """
        element = self.getElement(locator, locatorType)
        elementStatus = element.is_enabled()
        if elementStatus == True:
            self.log.info("Element with locator: " + locator + " is enabled.")
        elif elementStatus == False:
            self.log.info("Element with locator: " + locator + " is NOT enabled.")
        return elementStatus

    def getPageTitle(self):
        return self.driver.title


    def webScroll(self, value, direction="down"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, {}});".format(value))

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, {});".format(value))

    def mouseHover(self, locator, locatorType="xpath"):
        actions = ActionChains(self.driver)
        elementToHover = self.getElement(locator, locatorType)
        actions.move_by_offset(0, 0).perform()
        actions.move_to_element(elementToHover).perform()
        self.log.info("Hoovering on element :: " + locator)

    def selectFromDropDownWithKeys(self, element, selection):
        self.elementClick(element)
        dropDown = self.getElement(element)
        try:
            for i in range(0, selection):
                dropDown.send_keys(Keys.ARROW_DOWN)
                self.log.info("Moving down on dropdown by: " + str(i + 1))
            dropDown.send_keys(Keys.ENTER)
        except:
            self.screenShot("DropDownSelectionFailed")
            self.log.error("Moving down on dropdown list failed")

    # def webScrollToElement(self, locator, locatoryType="xpath"):
    #     element = self.getElement(locator, locatoryType)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true)", element)

    def webScrollToElement(self, locator, locatorType="xpath"):
        ActionChains(self.driver).move_to_element(self.getElement(locator, locatorType)).perform()


    def getAttributeValue(self, attribute, locator, locatorType="xpath"):
        element = self.getElement(locator, locatorType)
        elementAttributeValue = element.get_attribute(attribute)
        self.log.info("Locator: '" + locator + "' attribute value = " + elementAttributeValue)
        return elementAttributeValue

    def checkFieldMaxLenght(self, maxLenght, charNumber, locator, locatorType="xpath"):
        """
        Létrehoz egy 'maxlenght' hosszú random karaktersorozatot + 1 karaktert (a plusz karatkernek nem szabadna belekerülnie az input mezőbe)
        összehasonlítja a maxHossz + 1 karakterek hosszát a beírt karakterek hosszával
        maxLenght: Field max hossza, bussinnes logic alapján
        charNumber: Beütni kívánt karakterek száma
        """
        inputChars = self.util.getAlphaNumeric(charNumber, "mix")
        self.sendKeys(inputChars, locator, locatorType)
        self.log.info("Random chars: " + inputChars)
        # With attribute "value" it gives back the characters in the input field
        wroteText = self.getAttributeValue("value", locator, locatorType)
        self.log.info("Wrote chars: " + wroteText)
        assert maxLenght == len(wroteText)

    def rowCountInTable(self, locator, locatorType="xpath", headerRows=0):
        # Counts the rows in table
        # headerRows: Skip the given rows. Useful if there is a header row
        rows = len(self.getElementList(locator, locatorType))
        self.log.info("Rows in table = " + str(rows - headerRows))
        return rows

    def columnCountInTable(self, tableXpath, rowColumnCount=0):
        # Return the width of a table
        # rowColumnNum: From which row should we count the columns
        columns = len(self.getElementList(tableXpath + "/tbody/tr[" + str(rowColumnCount) + "]/td", "xpath"))
        self.log.info("Columns in table = " + str(columns))
        return columns

    def getSizeofTable(self, locator, locatorType, headerRows=0, rowColumnCount=0):
        return {"Rows": self.rowCountInTable(locator, locatorType, headerRows),
                "Columns": self.columnCountInTable(rowColumnCount)}

    def getAllData(self):
        allData = []
        rowNum = self.rowCountInTable("//tbody/tr", "xpath")
        columnWidth = self.columnCountInTable()
        for i in range(0, rowNum):
            ro = []
            for j in range(1, columnWidth):
                element = self.getElement("//tbody/tr[" + str(i + 1) + "]/td[" + str(j) + "]", "xpath")
                text = element.text
                text = text.strip()
                ro.append(text)
            allData.append(ro)
        self.log.info("Alldata: " + str(allData))
        return allData

    def presence_of_data(self,data , locator, locatorType="xpath"):
        dataSize = len(self.getElement("//*[contains(text(),'" + data + "')]", "xpath"))
        presence = False
        if dataSize > 0:
            presence = True
            self.log.info("The following data is presence :: " + data)
        else:
            self.log.info("The following data is not presence :: " + data)
        return presence

    def getRowData(self, tableXpath, columnWidth, rowNum=1, headerRow=1, locatorType="xpath"):
        #self.log.debug("Method " + str(__name__) + " started")
        rowData = []
        rowElements = self.getElementList(tableXpath + "//tr[" + str(rowNum + headerRow) + "]/td", locatorType)
        for rowElement in range(columnWidth):
            elementText = rowElements[rowElement].text
            rowData.append(elementText)
        self.log.info("Data in row number :: " + str(rowNum) + " is: " + str(rowData))
        return rowData


    def getColumnData(self, tableXpath, column, rowsInColumn, headerRow=0, locatorType="xpath", infoText=""):
        columnData = []
        columnElements = self.getElementList(tableXpath + "//tr/td[" + str(column) + "]")
        for columnElement in range(rowsInColumn):
            elementText = columnElements[columnElement].text
            columnData.append(elementText)
        self.log.info("Data in column number :: " + str(column) + " is: " + str(columnData) + " " + infoText)
        return columnData


    def tableColumnSorterCheck(self, tableXpath, column, rowsInColumn, sortingBtnLocator, sortingBtnLocatorType="xpath", numberOfClicks=1, sortMethod="asc"):
        unsortedColumnData = self.getColumnData(tableXpath, column, rowsInColumn)
        sortedList = self.util.sortingList(list=unsortedColumnData, method=sortMethod)
        for i in range (0, numberOfClicks):
            self.elementClick(sortingBtnLocator, sortingBtnLocatorType)
        sortedListByWeb = self.getColumnData(tableXpath, column, rowsInColumn)
        if sortMethod == "asc":
            self.log.info("The list is ascending")
        else:
            self.log.info("The list is descending")
        self.log.info("The two lists are equal.")
        self.log.info("List sorted by code :: " + str(sortedList))
        self.log.info("List sorted by web :: " + str(sortedListByWeb))
        if sortedList == sortedListByWeb:
            return True
        else:
            return False

#//table[@id='myTable2']//tr/td[1]
        # unsortedColumnData = self.basePage.getColumnData(tableXpath=self.appUsersPage._appUsersTable, column=1, rowsInColumn=3, infoText="Raw column data")
        # descSortedList = self.util.sortingList(list=unsortedColumnData, method="desc")
        # self.appUsersPage.clickOnNameFilter()
        # descSort = self.basePage.getColumnData(tableXpath=self.appUsersPage._appUsersTable, column=1, rowsInColumn=3, infoText="Desc sort by web")
        # assert descSortedList == descSort

    def getPageTitle(self):
        actualTitle = self.driver.title
        self.log.info("The page title is: " + str(actualTitle))
        return actualTitle


    def assertTitle(self, actualTitle, exceptedTitle):
        self.log.debug("Title assertation function started")
        self.log.debug("Actual title :: " + str(actualTitle))
        self.log.debug("exceptedTitle :: " + str(exceptedTitle))
        if actualTitle == exceptedTitle:
            self.log.debug("Title assert True")
            return True
        else:
            self.log.debug("Title assert False")
            return False

    ### Select option(s) from dropdown

    def selectFromDropdownByVisibleText(self, visibleText, locator, locatorType="xpath"):
        dropDownElement = Select(self.getElement(locator, locatorType))
        dropDownElement.select_by_visible_text(visibleText)
        self.log.info("Option with visible text:: " + str(visibleText) + " :: selected from dropdown")

    def selectFromDropdownByIndex(self, index, locator, locatorType="xpath"):
        dropDownElement = Select(self.getElement(locator, locatorType))
        dropDownElement.select_by_index(index)
        self.log.info("Option with index :: " + str(index) + " :: selected from dropdown")

    def selectFromDropdownByValue(self, value, locator, locatorType="xpath"):
        dropDownElement = Select(self.getElement(locator, locatorType))
        dropDownElement.select_by_value(value)
        self.log.info("Option with value :: " + str(value) + " :: selected from dropdown")

    def getParentRowElementsByChildFromTable(self, elementText):
        """
        "//td[contains(text(), 'List test 3')]//parent::tr"
        :param elementText: Text on child element (text in a record)
        :return: List of elements from the parent (all elements from the childs row)
        """
        tableRowElements = []
        elementsInRow = self.getElementList("//td[contains(text(), '" + str(elementText) +
                                        "')]//parent::tr/td[@class='MuiTableCell-root MuiTableCell-body material-table__cell']")
        self.log.info("list len " + str(len(elementsInRow)))
        for elements in range(1, len(elementsInRow)):
            textInElement = elementsInRow[elements].text
            self.log.debug("textOnElement: " + textInElement)
            tableRowElements.append(textInElement)
        self.log.info("Elements in row :: " + str(tableRowElements) + " from child: " + str(elementText))
        return tableRowElements






















