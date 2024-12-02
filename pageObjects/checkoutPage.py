from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckoutPage:

    # Yapıcı metod, driver'ı sınıfa bağlar
    def __init__(self, driver):
        self.driver = driver

    # Kart başlıkları için XPATH seçici
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    # Kartın alt kısmı için XPATH seçici
    cardFooter = (By.XPATH, "div/h4/a")
    # Checkout butonu için XPATH seçici
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    # Kart başlıklarını döndüren metod
    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    # Kartın alt kısmını döndüren metod
    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    # Checkout işlemini başlatan metod
    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        # ConfirmPage nesnesini oluşturur ve döner
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

