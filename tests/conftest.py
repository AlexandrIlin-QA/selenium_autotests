"""
Fixture
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """
    Main fixture
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sendbox") 
    chrome_options.add_argument("start-maximized") # открыть браузер в максимальном размере
    chrome_options.add_argument("--disable-infobars") # отключить инфотабы
    chrome_options.add_argument("--disable-extensions") # отключить расширения
    # chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()