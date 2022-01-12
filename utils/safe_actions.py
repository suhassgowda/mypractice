import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config import Config
from src.base.BrowserSetup import logger
from src.utils.assertions import Assertions


class SafeActions(Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_until_visible(self, locator=None, timeout=None):
        """
        This method waits until element to be visible.

        Parameters:
            locator: element locator
            timeout: time to wait for element to be visible

        Returns: element
        """
        global element
        try:
            logger.info(f"Waiting for {timeout} until {locator} is visible")
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator))
        except NoSuchElementException:
            logger.error(f"{locator} not found in {timeout}")
            logger.exception("No Such Element Exception")
        except TimeoutException:
            logger.error(f"{locator} not found in {timeout}")
            logger.exception("Time Out Exception")
        return element

    def wait_until_clickable(self, locator=None, timeout=None):
        """
        This method waits until element is clickable

        Parameters:
            locator: element locator
            timeout: time to wait for element to be clickable

        Returns: element
        """
        global element
        try:
            logger.info(f"Waiting for {timeout} until {locator} is clickable")
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        except NoSuchElementException:
            logger.error(f"{locator} not found in {timeout}")
            logger.exception("No Such Element Exception")
        except TimeoutException:
            logger.error(f"{locator} not found in {timeout}")
            logger.exception("Time Out Exception")
        return element

    def safe_click(self, locator=None, timeout=30):
        """
        This method waits until element to be clickable and clicks element

            Parameters:
                   locator: element locator
                   timeout: time to wait for element to be clickable

            Returns: element
            """
        web_element = self.wait_until_clickable(locator, timeout)
        try:
            # self.highlight(web_element)
            web_element.click()
            logger.info(f"Clicked on {locator}")
        except NoSuchElementException:
            logger.error(f"{locator} not found in {timeout}")
            logger.exception("No Such Element Exception")
        except TimeoutException:
            logger.error(f"{locator} not found in {timeout}")
            logger.exception("Time Out Exception")
        return web_element

    def get_text(self, locator=None):
        """
        This method gets element text

            Parameters:
                   locator: element locator

            Returns: text
            """
        self.wait_until_visible(locator, 50)
        if type(locator) == tuple:
            return self.driver.find_element(*locator).text
        else:
            return self.driver.find_element(locator).text

    def highlight(self, web_element):
        """Highlights (blinks) a Selenium Webdriver element"""

        # driver = element._parent
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                       web_element, s)

        apply_style("border: {0}px solid {1};".format(1, "red"))

    def safe_js_click(self, web_element):
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)
        self.driver.execute_script("arguments[0].click();",
                                   web_element)

    def safe_js_click(self, locator=None, timeout=30):
        """
        This method waits until element to be clickable and clicks element

            Parameters:
                   locator: element locator
                   timeout: time to wait for element to be clickable

            Returns: element
            """
        web_element = self.wait_until_visible(locator, timeout)
        try:
            # self.highlight(web_element)
            self.driver.execute_script("arguments[0].click();",
                                       web_element)
            logger.info(f"Clicked on {locator}")
        except NoSuchElementException:
            logger.error(f"{locator} not found in {timeout}")
            logger.exception("No Such Element Exception")
        return web_element

    def safe_enter_text(self, locator=None, text=None, timeout=None):
        """
        This method waits for element to visible and enters text

            Parameters:
                   locator: element locator
                   text: text to enter in input field
                   timeout: time to wait for element to be visible
            """
        try:
            input_element = self.wait_until_visible(locator, timeout)
            # self.highlight(input_element)
            # input_element.click()
            #
            input_element.send_keys(text)
            logger.info(f"Entered {text} into element {locator} ")
        except Exception as e:
            logger.exception(e)
            logger.error(f"Could not enter {text} into {locator}")
            assert False, f"Could not enter {text} into {locator}"

    def get_title(self):
        """ This method returns page title"""
        return self.driver.title

    @staticmethod
    def wait_for_time(wait_in_seconds):
        """ This method returns page url"""
        logger.info(f"Waiting for {wait_in_seconds} seconds")
        time.sleep(wait_in_seconds)

    def get_url(self):
        """ This method returns page url"""
        return self.driver.current_url

    def wait_for_presence_of_all_elements_located(self, locator, wait_in_seconds):
        wait = WebDriverWait(self.driver, wait_in_seconds)
        from selenium.webdriver.support import expected_conditions as ec
        wait.until(ec.presence_of_all_elements_located(locator))
        logger.info(f"Waiting for presence of all elements located seconds")
        return True

    def safe_wait_for_presence_of_all_elements_located(self, locator, wait_in_seconds):
        value = False
        try:
            wait = WebDriverWait(self.driver, wait_in_seconds)
            from selenium.webdriver.support import expected_conditions as ec
            wait.until(ec.presence_of_all_elements_located(locator))
            logger.info(f"Waiting for presence of all elements located seconds")
            value = True
        except TimeoutException:
            pass
        return value

    def safe_click_from_list_of_elements(self, locator, element_text, wait_in_seconds):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        try:
            self.wait_for_presence_of_all_elements_located(locator, wait_in_seconds)
        except TimeoutException:
            pass
        element_list = self.driver.find_elements(*locator)
        if len(element_list) == 0:
            full_name = "null"
        else:
            for web_element in element_list:
                if web_element.text.upper().__contains__(str(element_text).upper()):
                    full_name = web_element.text
                    web_element.click()
                    logger.info(f"Clicked on {locator} with {element_text}")
                    break
        return full_name


    def safe_js_click_from_list_of_elements(self, locator, element_text, wait_in_seconds):
        try:
            self.wait_for_presence_of_all_elements_located(locator, wait_in_seconds)
        except TimeoutException:
            pass
        element_list = self.driver.find_elements(*locator)
        if len(element_list) == 0:
            full_name = "null"
        else:
            for web_element in element_list:
                if web_element.text.upper().__contains__(str(element_text).upper()):
                    full_name = web_element.text
                    self.safe_js_click(web_element)
                    logger.info(f"Clicked on {locator} with {element_text}")
                    break
        return full_name

    def is_element_displayed(self, locator):
        value = False
        try:
            value = self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            pass
        return value