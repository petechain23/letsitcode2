import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # _search_box = "search-courses"
    # _search_course_icon = "search-course-button"
    # _course = "//div[contains(text(),'JavaScript for beginners')]"
    # _all_courses = "//div[@class='course-listing']"
    # _enroll_button = "enroll-button-top"
    # _cc_num = "//input[@aria-label='Credit or debit card number']"
    # _cc_exp = "exp-date"
    # _cc_cvv = "cvc"
    # _zip_code = "billingPostalCode"
    # _submit_enroll = "//span[contains(text(),'Buy Now')]"

    _search_box = "course"
    _search_course_icon = "//i[@class='fa fa-search']"
    _course = "//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
    _all_courses = '//*[@id="course-list"]'
    _enroll_button = "//div[3]/button"
    _cc_num = "cardnumber"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    # _zip_code = "billingPostalCode"
    _submit_enroll = "/html/body/div[1]/div[3]/div/div/div[1]/div[1]/p"

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="name")
        self.elementClick(locator=self._search_course_icon, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        time.sleep(3)
        self.SwitchFrameByIndex(self._cc_num, locatorType="name")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="name")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    # def enterZip(self, zip):
    #     self.switchToFrame(name="__privateStripeFrame7")
    #     self.sendKeys(zip, locator=self._zip, locatorType="name")
    #     self.switchToDefaultContent()

    # def clickAgreeToTermsCheckbox(self):
    #     self.elementClick(locator=self._agree_to_terms_checkbox)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        # self.enterZipCode(zipCode)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        time.sleep(5)
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result
