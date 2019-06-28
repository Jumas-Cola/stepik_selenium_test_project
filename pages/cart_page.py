from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_FORMSET),\
            'Basket is not empty, but should be.'

    def should_not_be_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.BASKET_FORMSET),\
            'Basket is empty, but should not be.'

    def should_be_empty_cart_text(self):
        assert self.is_element_present(
            *CartPageLocators.BASKET_EMPTY_TEXT),\
            "Empty cart text is not presented, but should be."

    def should_not_be_empty_cart_text(self):
        assert self.is_not_element_present(
            *CartPageLocators.BASKET_EMPTY_TEXT),\
            "Empty cart text is presented, but should not be."
