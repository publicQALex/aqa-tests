import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver (request):
    options = Options()
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()