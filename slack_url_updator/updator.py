import os
import time 
from dotenv import load_dotenv
from selenium import webdriver
from ngrok_wrapper.ngrok import TunnelNg
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


load_dotenv()

# SLACK CREDENTIAL 
SLACK_PASSWORD = os.environ.get("SLACK_PASSWORD")
SLACK_USERNAME = os.environ.get("SLACK_USERNAME")

# NGROK KEY
NGROK_PORT = os.environ.get('NGROK_PORT')
NGROK_AUTH_TOKEN = os.environ.get('NGROK_AUTH_TOKEN')
NGROK_REQUEST_TYPE = os.environ.get('NGROK_REQUEST_TYPE')


TOGGLE_EVENT = "//div[@class='ts_toggle_button']"
LOGIN_URL = "https://team-next-world.slack.com/sign_in_with_password"
SUBSCRIPTIONS_URL = "https://api.slack.com/apps/A04HF34TGHF/event-subscriptions?"


class SlackUrlUdater:
    def __init__(self, slack_cred):
        self.username = slack_cred['USERNAME']
        self.password = slack_cred['PASSWORD']
        self.url = LOGIN_URL
        self.req_url_suffix = '/slack/events'
        self.chrome_options = Options()
        self.web_driver_params = {
        'options': self.chrome_options
        }
        self.chrome_options.add_argument('start-maximized')
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = self.get_driver()

    def get_driver(self):
        return webdriver.Chrome(ChromeDriverManager().install(),**self.web_driver_params)

    def login_credentials(self):
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(self.username)
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
        time.sleep(10)
    
    def event_subscription(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(SUBSCRIPTIONS_URL)
        # self.driver.find_element(By.XPATH,"//div[@class='ts_toggle_button']").click()

    def request_url_in_event_subscription(self, req_url):
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//button[@id='change_request_url']").click()
        self.driver.find_element(By.XPATH,"//input[@id='request_url']").send_keys(req_url)
        time.sleep(15)
        self.driver.find_element(By.XPATH,"//button[@data-qa='save_changes_button']").click()

    def update_request_url(self, req_url):
        self.driver = self.get_driver()
        self.driver.get(self.url)
        self.driver.execute_script("window.open('');")
        time.sleep(10)
        self.login_credentials()
        self.event_subscription()
        self.request_url_in_event_subscription(req_url + self.req_url_suffix)
        self.driver.quit()


def updator():
    slack_cred = {
        'USERNAME': SLACK_USERNAME,
        'PASSWORD': SLACK_PASSWORD,
    }

    ngrok_key = {
        'PORT': NGROK_PORT,
        'AUTH_TOKEN': NGROK_AUTH_TOKEN,
        'REQUEST_TYPE': NGROK_REQUEST_TYPE
    }

    slack_url_updator = SlackUrlUdater(slack_cred)

    TunnelNg(ngrok_key, slack_url_updator.update_request_url).poll_tunnels()

    
if __name__ == "__main__":
    updator()
