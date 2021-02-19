from base.selenium_drivers import SeleniumDrivers
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDrivers):


    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def doScreenshot(self, resultMessage):
        self.screenShot(resultMessage)
        self.log.info("Screenshot " + resultMessage + "done")

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getPageTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to verify " + titleToVerify + " title")
            print_stack()
            return False

    def getTextFromInputField(self, locator, locatorType="xpath"):
        """
        Get the text from an input field
        :return: String. Text from an input field
        """
        textOnElement = self.getTextByAttribute(locator, locatorType)
        return textOnElement

    def getTextFromMultiSelectField(self, locatorName, locatorType="xpath"):
        """
        Get text from ONLY one element from the multiselect field.
        :return: String. Text from the element
        """
        textOnElement = self.getText("//span[contains(text(), '" + locatorName + "')]//parent::div//div[@class='multiple-search-select__label']", locatorType)
        return textOnElement

    def verifyText(self, actualText, exceptedText, locatorType="xpath"):
        """
        Verify that the element text is exactly the same as the excepted element
        :param actualText: Text from a web element
        :param exceptedText: Text what we want to verify on element
        :return: Boolean. True if texts match, False if not
        """
        textOnElement = self.getText(actualText, locatorType)
        result = self.util.verifyTextMatch(textOnElement, exceptedText)
        return result
