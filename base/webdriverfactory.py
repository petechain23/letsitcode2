from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = "https://courses.letskodeit.com/"
        # baseUrl = "https://letskodeit.teachable.com/"
        if self.browser == 'firefox':
            '''Start Handle Security check for chrome'''
            # profile = webdriver.FirefoxProfile()
            # profile.accept_untrusted_certs = True
            # driver = webdriver.Firefox(firefox_profile=profile)
            '''Stop'''
            driver = webdriver.Firefox()
            print("Running tests on FF")
        elif self.browser == 'chrome':
            '''Start Handle Security check for chrome'''
            # opt = webdriver.ChromeOptions()
            # opt.add_argument("/private/var/folders/fg/311wcjnn2nqd9nv4s7zzt5d40000gn/T/.com.google.Chrome.Y08LbJ/Default")
            # driver = webdriver.Chrome(options=opt)
            '''Stop '''
            driver = webdriver.Chrome()
            print("Running tests on chrome")
        else:
            driver = webdriver.Safari()
            print("Running tests on Safari")

        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)
        return driver
