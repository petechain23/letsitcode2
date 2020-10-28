from pages.course.register_courses_page import RegisterCoursesPage
import unittest
import pytest
from utilities.checkstatus import CheckStatus
import time
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseCSVTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = CheckStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourse()
        time.sleep(5)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/dattran/Documents/Virtualenv/PyCharm/workspace_python/letskodeit/data.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        time.sleep(2)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(2)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(5)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")