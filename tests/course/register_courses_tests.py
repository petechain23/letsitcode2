from pages.course.register_courses_page import RegisterCoursesPage
import unittest
import pytest
from utilities.checkstatus import CheckStatus
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="4450900412345678", exp="1220", cvv="123")
        time.sleep(5)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")