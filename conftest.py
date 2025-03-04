import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                    help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', 
                    help='Select language')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lang_name = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":  
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang_name})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', lang_name)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print(f"\nstart {browser_name} browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()