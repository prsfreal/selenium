#conftest is a fixture for the test classes(test suites)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.firefox.options import Options as FFO
import pytest
from datetime import datetime


#Capture the command line input and pass to fixture
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


#Open correct driver and close after each test
@pytest.fixture()
def setupandteardown(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'chromeless':
        chrome_options = CO()
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

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

    yield driver

    driver.close()




#TODO PYTEST HTML REPORT
#Add rows to the Environment table HTML data
def pytest_configure(config):
    config._metadata['Project Name'] = 'Validate Services'

#Remove from HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    pass

#Set the title of the report
def pytest_html_report_title(report):
    report.title = datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')

