from pages.course.register_courses_page import RegisterCoursesPage
import unittest
import pytest
from utilities.checkstatus import CheckStatus
import time
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseMutipleDataSet(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4450900412345678", "1220", "123"), ("Selenium WebDriver Advanced", "4450900412345678", "1220", "124"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(5)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

        self.driver.find_element_by_link_text("ALL COURSES").click()