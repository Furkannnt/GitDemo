import time
from itertools import product
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkoutPage import CheckoutPage
from pageObjects.homePage import HomePage
from utilities.baseClass import baseClass


#@pytest.mark.usefixtures("setup")
class TestOne(baseClass):

    def test_e2e(self):
        # Logger'ı alın
        log = self.getLogger()
        # Ana sayfa nesnesi oluşturun
        homePage = HomePage(self.driver)
        # Ürünlerin bulunduğu sayfaya gidin
        checkoutPage = homePage.shopItems()
        log.info("getting all the card titles")
        # Tüm kart başlıklarını alın
        cards = checkoutPage.getCardTitles()
        i = -1
        # Kart başlıkları arasında dolaşın
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            # Başlık "Blackberry" ise, sepete ekle
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        # Alışveriş sepetine gidin
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        # Onay sayfasına gidin
        confirmpage = checkoutPage.checkOutItems()
        log.info("Entering country name")

        # Ülke adını girin
        self.driver.find_element(By.ID, "country").send_keys("Tur")
        # Türkiye linkinin görünmesini bekleyin ve tıklayın
        self.verifyLinkPresence("Turkey")
        self.driver.find_element(By.LINK_TEXT, "Turkey").click()
        # Onay kutusunu işaretleyin
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        # Formu gönderin
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Başarı mesajını alın
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Received text is" + message)
        # Başarı mesajının "Success!" içerdiğini doğrulayın
        assert "Success!" in message

        # Bir süre bekleyin
        time.sleep(3)




























