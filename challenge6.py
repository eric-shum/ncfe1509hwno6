import unittest, re, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common2.TopNavSearch import TopNavSearch
from common2.Filters import Filters
from common2.Screenshot import Screenshot


class challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.driver.maximize_window()
        s = TopNavSearch(self.driver)
        f = Filters(self.driver)
        ss = Screenshot(self.driver)

        try:
            filterName = "Model"
            modelvalue = "Maxima G"
            query = "Nissan"
            self.assertIn(query.upper(), s.runSearch(query).text)
            # runheadersearch
            txtelement, count = f.openFilterSection(filterName)

            txtelement.send_keys(modelvalue)

            checkElement = self.driver.find_element(By.XPATH,
                "//*[@id='collapseinside" + str(count) + "']//abbr[@value='" + modelvalue + "']")
            checkElement.click()

        except:
            print("An exception occurred")
            # capture an image
            print("You wanted " + modelvalue)

            timestr = time.strftime("%Y%m%d-%H%M%S")

            element = self.driver.find_element(By.XPATH, "//*[@id='filters-collapse-1']")

            filelocation = "../screenshots/image_" + timestr + ".png"

            ss.capture(element, filelocation)

            # grab these checkboxes
            checkboxelements = self.driver.find_elements(By.XPATH,
                "//*[@id='collapseinside" + str(count) + "']//input[@type='checkbox']")
            print(" but these are the available checkboxes")
            for e in checkboxelements:
                print(e.get_attribute('value'))

