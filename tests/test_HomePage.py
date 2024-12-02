import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from TestData.HamePageData import HomePageData
from pageObjects.homePage import HomePage
from utilities.baseClass import baseClass

class TestHomePage(baseClass):

    @pytest.mark.parametrize("getData", HomePageData.get_test_data("C:/Users/PROVEN-LAPTOP/Desktop/pythonGetData.xlsx"))
    def test_formSubmission(self, getData):
        log = self.getLogger()  # Logger oluştur
        homepage = HomePage(self.driver)  # HomePage nesnesi oluştur

        # Form alanlarını doldur
        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["mail"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckBox().click()

        # Cinsiyet seçeneğini seç
        self.selectOptionByText(homepage.select(), getData["gender"])

        # Formu gönder ve sonucu kontrol et
        self.clickable("//input[@type='submit']")
        homepage.submitForm().click()

        # Başarı mesajını doğrula
        self.verifyMessage("div.alert-success")
        alertText = homepage.getMessage().text
        log.info("Message is " + alertText)
        assert "Success" in alertText

        # Sayfayı yenile
        self.driver.refresh()

        time.sleep(2)  # Kısa bir süre bekle
