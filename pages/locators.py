from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BOOK_NAME = (By.CSS_SELECTOR, 'h1')
    BOOK_NAME_ON_MSG = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    PRICE = (By.CSS_SELECTOR, '#content_inner .product_main > p.price_color')
    PRICE_ON_MSG = (By.CSS_SELECTOR,
                    '#messages > .alert-info.fade.in p:nth-child(1) > strong')
    SUCCESS_MSG = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > .alert-info.fade.in > div strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "div.basket-mini a")


class CartPageLocators:
    BASKET_FORMSET = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
