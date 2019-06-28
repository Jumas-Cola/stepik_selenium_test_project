from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import random
import pytest
import time


class TestUserAddToCartFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + '@fakemail.org'
        password = pass_generate()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_msg()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_success_msg()
        page.should_be_same_names()
        page.should_be_basket_price()
        page.should_be_same_prices()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_msg()
    page.should_be_same_names()
    page.should_be_basket_price()
    page.should_be_same_prices()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_card_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_empty_cart_text()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason='Guest should see success message after adding product to cart.')
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_msg()


@pytest.mark.xfail(reason='Success message shouldnt dessapears.')
def test_message_dissapeared_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_msg()


@pytest.mark.xfail(reason='Guest shouldnt see product in basket if he dont added it.')
def test_guest_can_see_product_in_cart_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_card_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_empty_cart()
    cart_page.should_not_be_empty_cart_text()


def pass_generate(nums=3, chars=5, caps=2, signs=2):
    password = []
    for i in range(nums):
        password += random.choice([*'0123456789'])
    for i in range(chars):
        password += random.choice([chr(i) for i in range(97, 123)])
    for i in range(caps):
        password += random.choice([chr(i) for i in range(65, 91)])
    for i in range(signs):
        password += random.choice([*r'!@#$%^&*_=+-/"[](){}'])
    random.shuffle(password)
    return ''.join(password)
