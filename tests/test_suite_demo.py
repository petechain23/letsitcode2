import unittest
from tests.course.register_courses_csv_data import RegisterCourseCSVTests
from tests.home.login_tests import LoginTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseCSVTests)

smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=1).run(smokeTest)