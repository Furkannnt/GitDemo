import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class baseClass:

    # Logger oluşturma metodu
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log', encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # FileHandler nesnesini logger'a ekler
        logger.setLevel(logging.DEBUG)
        return logger

    # Bir linkin sayfada mevcut olup olmadığını doğrulayan metod
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    # Bir öğenin tıklanabilir olup olmadığını doğrulayan metod
    def clickable(self, text):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, text))
        )

    # Bir mesajın sayfada mevcut olup olmadığını doğrulayan metod
    def verifyMessage(self, text):
        alert = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, text)))

    # Bir dropdown menüsünden belirli bir metin seçen metod
    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        if text == "Male":
            sel.select_by_visible_text("Male")
        else:
            sel.select_by_visible_text("Female")






























