from base.selenium_drivers import SeleniumDrivers
import utilities.custom_logger as cl
import logging

class TestStatus(SeleniumDrivers):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result is True:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED 1:: " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED BECAUSE RESULT IS NOT BOOLEAN:: " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### EXCEPTION Occured!")
            self.screenShot(resultMessage)


    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in test case
        """
        self.setResult(result, resultMessage)


    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This should be a final test status of the test case
        """
        self.setResult(result, resultMessage)
        self.log.info("Test results are: " + str(self.resultList))

        if "FAIL" in self.resultList:
            self.log.error(testName + "### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True

