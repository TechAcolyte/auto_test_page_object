from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
    
    def should_be_success_add_to_basket(self):
        title_product = self.get_text_of_element(*ProductPageLocators.TITLE_PRODUCT)
        message_success_add_to_basket = self.get_text_of_element(*ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET)

        price_product = self.get_text_of_element(*ProductPageLocators.PRICE_PRODUCT)
        message_price_add_to_basket = self.get_text_of_element(*ProductPageLocators.MESSAGE_PRICE_ADD_TO_BASKET)

        assert self.compare_text(title_product, message_success_add_to_basket)
        assert self.compare_text(price_product, message_price_add_to_basket)