from time import sleep
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


# def test_guest_can_add_product_to_cart(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_be_success_msg()
#     name = page.get_book_name()
#     name_from_msg = page.get_book_name_from_msg()
#     page.should_be_same_names(name, name_from_msg)
#     price = page.get_price()
#     price_from_msg = page.get_price_from_msg()
#     page.should_be_same_price(price, price_from_msg)

#
# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     assert page.is_not_element_present(
#         *ProductPageLocators.SUCCESS_MSG), 'Element present, but shouldnt.'
#
#
# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     assert page.is_not_element_present(
#         *ProductPageLocators.SUCCESS_MSG), 'Element present, but shouldnt.'
#
#
# def test_message_dissapeared_after_adding_product_to_cart(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     assert page.is_disappeared(
#         *ProductPageLocators.SUCCESS_MSG), 'Element present, but shouldnt.'
