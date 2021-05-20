from .locators import ProductPageLocators
from .base_page import BasePage
import time


class PageObject(BasePage):

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        link.click()

    def touch_button(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON)
        link.click()
        # assert "The shellcoder's handbook has been added to your basket" in

    def just_name(self):
        # link = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        # link.click()
        name_exc = self.browser.find_element(*ProductPageLocators.NAME_BOOK_STR).text
        name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_BASKET).text
        assert name_exc == name

    def just_price(self):
        # link = self.browser.find_element(*ProductPageLocators.PRICE)
        # link.click()
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_STR).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_book == price_basket
