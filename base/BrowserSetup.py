import logging
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import __root__
from Config import Config
from src.utils.custom_logger import custom_logger

logger = custom_logger(logging.DEBUG)


def parse_chrome_options(opts: str):
    return opts.split("|")


class BrowserSetup(unittest.TestCase):
    """This is class is used to setup the browser actions"""

    rootPath = __root__.path()

    def setUp(self):
        if Config.BROWSER_NAME.upper() == Config.CHROME:
            chrome_options = Options()
            if Config.CHROME_OPTIONS:
                logger.info(f"Using the following CHROME_OPTIONS: {Config.CHROME_OPTIONS}")
                for chrome_arg in parse_chrome_options(Config.CHROME_OPTIONS):
                    chrome_options.add_argument(chrome_arg.strip())
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
            logger.info("Launched Chrome browser ")
        elif Config.BROWSER_NAME.upper() == Config.FIREFOX:
            # self.driver = webdriver.Firefox()
            self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install()
            )
            # self.driver = webdriver.Firefox()
            logger.info("Launched Firefox browser")
        elif Config.BROWSER_NAME.upper() == Config.SAFARI:
            self.driver = webdriver.Safari()
            logger.info("Launched Safari browser ")
        else:
            assert False, "Provide Browser name as Chrome or Firefox or Safari"
        self.driver.maximize_window()
        self.driver.get(Config.URL)
        logger.info("Navigated to {}".format(Config.URL))

    def screen_shot(self):
        """Take a Screen-shot of browser, when a testcase Failed."""
        test_status = "Pass"
        for method, error in self._outcome.errors:
            if error:
                test_status = "Fail"
                timestamp = time.asctime().replace(":", "_")
                screenshot_path = os.path.join(
                    __root__.path(),
                    "Reports/Screenshots/{}_{time}.png".format(
                        self._testMethodName, time=timestamp
                    ),
                )
                logger.info("Saving screenshot to {}".format(screenshot_path))
                self.driver.get_screenshot_as_file(screenshot_path)
                from pytest_html_reporter import attach

                attach(data=self.driver.get_screenshot_as_png())
                logger.info("FAILED - " + "{}".format(self._testMethodName) + "-" * 5)
        return test_status

    def tearDown(self):
        """CLose the browser"""
        test_status = self.screen_shot()
        if test_status.__contains__("Pass"):
            logger.info("PASSED - " + "{}".format(self._testMethodName) + "-" * 5)
        # self.driver.quit()
