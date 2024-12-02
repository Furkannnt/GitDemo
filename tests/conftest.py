import time
from email.policy import default
from itertools import product
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Küresel driver değişkenini tanımla
driver = None


# Komut satırı seçeneklerini pytest'a ekle
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# pytest fixture: test sınıfı başına bir kez çalıştırılır
@pytest.fixture(scope="class")
def setup(request):
    global driver
    # Komut satırı seçeneğinden tarayıcı adını al
    browser_name = request.config.getoption("browser_name")

    # Tarayıcıyı başlat
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-error")
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    # Web sitesine git ve pencereyi büyüt
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    # driver nesnesini request nesnesine ata
    request.cls.driver = driver
    yield
    driver.close()


# pytest raporunu oluşturma hook'u
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    # Test başarısız veya skip edilmişse ekran görüntüsü al
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# Ekran görüntüsü alma fonksiyonu
def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)































