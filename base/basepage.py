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

