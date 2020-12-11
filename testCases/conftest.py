from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.firefox.options import Options as FFO
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'chromeless':
        chrome_options = CO()
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        ###Optional arguments for Headless
        # chrome_options.headless = True
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox") # linux only
        # chrome_options.add_argument("--headless")

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'firefoxless':
        firefox_options = FFO()
        firefox_options.add_argument("-headless")
        driver = webdriver.Firefox(options=firefox_options)


    elif browser == 'safari':
        #safari does not like to run in parallel
        driver = webdriver.Safari()
        driver.set_window_size(1920, 1080)
    else:
        driver = webdriver.Chrome()

    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')



#TODO PYTEST HTML REPORT
#Customize HTML data
def pytest_configure(config):
    config._metadata['Project Name'] = 'non Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Philip'

#Remove from HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    #metadata.pop("Java_Home", None)
    #metadata.pop("Plugins", None)
    pass