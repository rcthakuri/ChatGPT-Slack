# URL - url based selector 
LOGIN_URL = "https://team-next-world.slack.com/sign_in_with_password"
SUBSCRIPTIONS_URL = "https://api.slack.com/apps/A04HF34TGHF/event-subscriptions?"

# XPATH - xpath based selector for slack event subscription
USERNAME = "//input[@id='email']"
PASSWORD = "//input[@id='password']"
LOGIN_BUTTON = "//button[normalize-space()='Sign In']"
SEND_KEYS_TO_REQUEST_URL = "//input[@id='request_url']"
CHANGE_REQUEST_URL_BUTTON = "//button[@id='change_request_url']"
SAVE_CHANGES_BUTTON = "//button[@data-qa='save_changes_button']"
NEW_REQUEST_URL_VERIFIED_CONTAINER = "//label[@for='new_request_url' and contains(., 'Verified')]"


class SlackSelector:
    def __init__(self):
        self.event_subscription_selector = EventSubscriptionSelector()


class EventSubscriptionSelector:

    def __init__(self):
        self.__EventSubscriptionSelector = {}
        self.init_event_subscription_selector()

    def init_event_subscription_selector(self):
        self.__EventSubscriptionSelector['username'] = USERNAME
        self.__EventSubscriptionSelector['password'] = PASSWORD
        self.__EventSubscriptionSelector['login_url'] = LOGIN_URL
        self.__EventSubscriptionSelector['login_button'] = LOGIN_BUTTON
        self.__EventSubscriptionSelector['subscription_url'] = SUBSCRIPTIONS_URL
        self.__EventSubscriptionSelector['save_changes_button'] = SAVE_CHANGES_BUTTON
        self.__EventSubscriptionSelector['send_keys_to_request_url'] = SEND_KEYS_TO_REQUEST_URL
        self.__EventSubscriptionSelector['change_request_url_button'] = CHANGE_REQUEST_URL_BUTTON
        self.__EventSubscriptionSelector['new_request_url_verified_container'] = NEW_REQUEST_URL_VERIFIED_CONTAINER

    def get_username(self) -> str:
        return self.__EventSubscriptionSelector['username']

    def get_password(self) -> str:
        return self.__EventSubscriptionSelector['password']

    def get_login_url(self) -> str:
        return self.__EventSubscriptionSelector['login_url']

    def get_login_button(self) -> str:
        return self.__EventSubscriptionSelector['login_button']

    def get_subscription_url(self) -> str:
        return self.__EventSubscriptionSelector['subscription_url']

    def get_save_changes_button(self) -> str:
        return self.__EventSubscriptionSelector['save_changes_button']

    def get_send_keys_to_request_url(self) -> str:
        return self.__EventSubscriptionSelector['send_keys_to_request_url']

    def get_change_request_url_button(self) -> str:
        return self.__EventSubscriptionSelector['change_request_url_button']

    def get_new_request_url_verified_container(self) -> str:
        return self.__EventSubscriptionSelector['new_request_url_verified_container']


