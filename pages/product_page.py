from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        btn.click()
        # self.solve_quiz_and_get_code()

    def should_be_success_msg(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MSG),\
            'Success message not present on the page'

    def should_not_be_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG),\
            'Success message is presented, but should not be'

    def should_be_basket_price(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRICE),\
            'Basket price not present on the page'

    def get_book_name(self):
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return name.text

    def get_book_name_from_msg(self):
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_MSG)
        return name.text

    def get_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        return price.text

    def get_price_from_msg(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_ON_MSG)
        return price.text

    def should_be_same_names(self):
        name = self.get_book_name()
        name_from_msg = self.get_book_name_from_msg()
        assert name == name_from_msg,\
            'Main book name and book name in message is not equal'

    def should_be_same_prices(self):
        price = self.get_price()
        price_from_msg = self.get_price_from_msg()
        assert price == price_from_msg,\
            'Main price and price in message is not equal'
