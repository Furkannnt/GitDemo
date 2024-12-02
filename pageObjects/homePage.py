from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.checkoutPage import CheckoutPage


class HomePage:

    # Yapıcı metod, driver'ı sınıfa bağlar
    def __init__(self, driver):
        self.driver = driver

    # Çeşitli sayfa öğeleri için seçiciler
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    # Alışveriş öğelerine gitme metod
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    # İsim alanını alma metod
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    # E-posta alanını alma metod
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    # Şifre alanını alma metod
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    # Onay kutusunu alma metod
    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    # Dropdown menüsünü alma metod
    def select(self):
        return self.driver.find_element(*HomePage.dropdown)

    # Formu gönderme metod
    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    # Başarı mesajını alma metod
    def getMessage(self):
        return self.driver.find_element(*HomePage.message)

        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def select(self):
        return self.driver.find_element(*HomePage.dropdown)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)













































