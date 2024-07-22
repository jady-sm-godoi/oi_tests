import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def home_url():
    return 'https://www.oi.com.br/grandes-empresas/'
