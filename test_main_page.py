from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_card_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_empty_cart_text()


@pytest.mark.xfail(reason='Guest shouldnt see product in basket if he dont added it.')
def test_guest_can_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_card_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_empty_cart()
    cart_page.should_not_be_empty_cart_text()
