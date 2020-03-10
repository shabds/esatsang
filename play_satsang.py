from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import datetime

# Following settings can be customized:
ESATSANG_USERNAME = "VSS2008012506557"
ESATSANG_PASSWORD = "1985-12-17"

MORNING_SATSANG_START_TIME = datetime.time(3, 0, 0)
MORNING_SATSANG_END_TIME = datetime.time(3, 0, 0)

EVENING_SATSANG_START_TIME = datetime.time(16, 0, 0)
EVENING_SATSANG_END_TIME = datetime.time(17, 0, 0)

OVERRIDE_TIME_RESTRICTIONS = False

# Define wait time between logins, in minutes
WAITING_PERIOD = 5

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode so no browser is launched
browser = Firefox(executable_path='depends\\geckodriver.exe', options=opts)


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def is_possible_satsang_time():
    return OVERRIDE_TIME_RESTRICTIONS or time_in_range(EVENING_SATSANG_START_TIME, EVENING_SATSANG_END_TIME,
                                                       datetime.datetime.now().time()) or time_in_range(
        MORNING_SATSANG_START_TIME,
        MORNING_SATSANG_END_TIME,
        datetime.datetime.now().time())


def is_login_open():
    if (is_possible_satsang_time()):
        # Not even going to attempt the login page if time not within specified range
        print(str(datetime.datetime.now()) + ': Current time within range. Launching login page.')
        browser.get('https://esatsang.itas.in/auth/login')
        content = browser.find_element_by_id('page-content')
        print(str(datetime.datetime.now()) + ': ' + str(content.text))
        return "Login is only allowed" not in str(content.text)
    print(str(datetime.datetime.now()) + ': Doing nothing as current time not within expected range.')
    return False


def play():
    if (is_login_open()):
        print(str(datetime.datetime.now()) + ': Attempting to login.')
        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")
        username.send_keys(ESATSANG_USERNAME)
        password.send_keys(ESATSANG_PASSWORD)
        browser.find_element_by_name("submit").click()
        browser.find_element_by_id('esatsang_live').click()
    else:
        print(str(datetime.datetime.now()) + ": Will check again in {} minutes...".format(WAITING_PERIOD))
        time.sleep(60 * WAITING_PERIOD)
        play()


play()
