from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    languages = {
    "de": "Ihr Warenkorb ist leer.",
    "en-gb": "Your basket is empty. Continue shopping",
    "ru": "Ваша корзина пуста"
    }
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "The cart is not empty"
    
    def should_be_empty_basket_message(self):
        text_element = self.get_text_of_element(*BasketPageLocators.BASKET_EMPTY)
        lang_attribute = self.browser.find_element(By.XPATH, "//html").get_attribute('lang')
        assert self.compare_text(self.languages.get(lang_attribute), text_element), "No message about empty basket"