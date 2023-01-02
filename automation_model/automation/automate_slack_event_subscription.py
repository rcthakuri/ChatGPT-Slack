import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from automation_model.selector.slack_selector import Selector


class SlackUrlUpdater:
    def __init__(self, slack_cred):
        self.username = slack_cred['USERNAME']
        self.password = slack_cred['PASSWORD']
        self.slack_update_selector = Selector()
        self.req_url_suffix = '/slack/events'
        self.chrome_options = Options()
        self.web_driver_params = {
        'options': self.chrome_options
        }
        self.chrome_options.add_argument('start-maximized')
        self.chrome_options.add_experimental_option('detach', True)
        self.url = self.slack_update_selector.event_subscription_selector.get_login_url()
        self.driver = self.get_driver()

    def get_driver(self):
        return webdriver.Chrome(ChromeDriverManager().install(),**self.web_driver_params)

    def login_credentials(self):
        self.driver.find_element(By.XPATH,self.slack_update_selector.event_subscription_selector.get_username()).send_keys(self.username)
        self.driver.find_element(By.XPATH,self.slack_update_selector.event_subscription_selector.get_password()).send_keys(self.password)
        self.driver.find_element(By.XPATH,self.slack_update_selector.event_subscription_selector.get_login_button()).click()
        time.sleep(10)
    
    def event_subscription(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.slack_update_selector.event_subscription_selector.get_subscription_url())
        # self.driver.find_element(By.XPATH,"//div[@class='ts_toggle_button']").click()

    def request_url_in_event_subscription(self, req_url):
        time.sleep(10)
        self.driver.find_element(By.XPATH,self.slack_update_selector.event_subscription_selector.get_change_request_url_button()).click()
        self.driver.find_element(By.XPATH,self.slack_update_selector.event_subscription_selector.get_send_keys_to_request_url()).send_keys(req_url)
        time.sleep(15)
        self.driver.find_element(By.XPATH,self.slack_update_selector.event_subscription_selector.get_save_changes_button()).click()

    def update_request_url(self, req_url):
        self.driver = self.get_driver()
        self.driver.get(self.url)
        self.driver.execute_script("window.open('');")
        time.sleep(10)
        self.login_credentials()
        self.event_subscription()
        self.request_url_in_event_subscription(req_url + self.req_url_suffix)
        self.driver.quit()