import time 
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

TOGGLE_EVENT = "//div[@class='ts_toggle_button']"
LOGIN_URL = "https://team-next-world.slack.com/sign_in_with_password"
SUBSCRIPTIONS_URL = "https://api.slack.com/apps/A04H4800L58/event-subscriptions?"


class SlackUrlUdate:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.url = LOGIN_URL
        self.chrome_options = Options()
        self.web_driver_params = {
        'options': self.chrome_options
        }
        self.chrome_options.add_argument('start-maximized')
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),**self.web_driver_params)
        self.driver.get(self.url)

    def login_credentials(self):
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(self.username)
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
        time.sleep(3)
    
    def event_subscription(self):
        self.driver.get(SUBSCRIPTIONS_URL)
        self.driver.find_element(By.XPATH,"//div[@class='ts_toggle_button']").click()

    def check_hourly(self):

        current_time = datetime.datetime.now()
        hour,min,sec = current_time.strftime("%H:%M:%S").split(':')
        total_time = int(hour) * 60 + int(min)
        while True: 
            time_checker = datetime.datetime.now()
            h,m,s = time_checker.strftime("%H:%M:%S").split(':')
            next_timer = int(h) * 60 + int(min)
            if total_time + 60 == next_timer:
                break




check = SlackUrlUdate("thapaanjan40@gmail.com","@slack@12345")
check.login_credentials()
check.event_subscription()
check.check_hourly()