# Selenium import and related lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

# Selector module
from automation.automation_model.selector.slack_selector import SlackSelector

# Other system lib import
import os
import warnings
from time import sleep
from typing import List, Any

# CONSTANT
GOOGLE_CHROME_PROFILE_DIR = ''
WAIT_DELAY = 6

warnings.filterwarnings("ignore")
os.environ['WDM_LOG_LEVEL'] = '0'  # Suppress web manager log


class CustomSelenium:
    def __init__(self):
        self.driver = None
        self.wait = WAIT_DELAY

    def __del__(self):
        if self.driver:
            print('Log -> Browser closed')
            self.driver.close()

    @staticmethod
    def selenium_cmd_handler(selenium_cmd, args, handle=False) -> Any:
        try:
            return selenium_cmd(*args)
        except Exception as e:
            if handle:
                print('Selenium Exception =>', e)
                return None
            else:
                raise e

    def wait_until_element_presence(self, by_object: By, selector, delay=None) -> \
            WebElement or TimeoutException:
        if not delay:
            delay = WAIT_DELAY
        try:
            element = WebDriverWait(self.driver, delay). \
                until(
                ec.presence_of_element_located(
                    (by_object, selector)))
            return element
        except TimeoutException:
            raise TimeoutException  # TODO, FIX IT

    def start_web_driver(self) -> 'REPLACE ME':  # FIXME:
        chrome_options = Options()
        # TOGGLE COMMENT FOR headless or !headless
        # chrome_options.add_argument("--headless")

        chrome_options.add_argument('log-level=3')
        chrome_options.add_argument('start-maximized')
        chrome_options.add_experimental_option('detach', True)
        if GOOGLE_CHROME_PROFILE_DIR:
            chrome_options.add_argument(r'user-data-dir=' + GOOGLE_CHROME_PROFILE_DIR)

        web_driver_params = {
            'options': chrome_options
        }

        self.driver = webdriver.Chrome(ChromeDriverManager().install(),
                                       **web_driver_params)
        self.driver.maximize_window()
        return self.driver


class SlackUrlUpdater(CustomSelenium):
    def __init__(self, slack_cred):
        super().__init__()
        self.username = slack_cred['USERNAME']
        self.password = slack_cred['PASSWORD']
        self.req_url_suffix = '/slack/events'
        self.url = self.slack_update_selector.get_login_url()
        self.slack_update_selector = SlackSelector().event_subscription_selector


    def login_to_slack(self):
        self.wait_until_element_presence(
            By.XPATH,
            self.slack_update_selector.get_username(),
            self.wait
            ).send_keys(self.username)
        self.driver.find_element(By.XPATH, self.slack_update_selector.get_password()).send_keys(self.password)
        self.driver.find_element(By.XPATH, self.slack_update_selector.get_login_button()).click()

    def go_to_event_subscription_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.slack_update_selector.get_subscription_url())
        # self.driver.find_element(By.XPATH,"//div[@class='ts_toggle_button']").click()

    def change_request_url_in_event_subscription_page(self, req_url):
        self.wait_until_element_presence(
            By.XPATH,
            self.slack_update_selector.get_change_request_url_button(),
            self.wait
            ).click()
        self.driver.find_element(By.XPATH, self.slack_update_selector.get_send_keys_to_request_url()).send_keys(req_url)
        self.wait_until_element_presence(
            By.XPATH,
            self.slack_update_selector.get_new_request_url_verified_container(),
            self.wait
        )
        self.wait_until_element_presence(
            By.XPATH,
            self.slack_update_selector.get_save_changes_button(),
            self.wait
        )

    def update_request_url(self, req_url):
        self.start_web_driver()
        self.driver.get(self.url)
        self.driver.execute_script("window.open('');")
        self.login_to_slack()
        self.go_to_event_subscription_page()
        self.change_request_url_in_event_subscription_page(req_url + self.req_url_suffix)
        self.driver.quit()
