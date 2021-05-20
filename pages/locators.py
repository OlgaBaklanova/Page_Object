from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, '#add_to_basket_form')
    BUTTON = (By.CLASS_NAME, "btn-group")
    NAME_BOOK_STR = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > h1')
    NAME_BOOK_BASKET = (By.CSS_SELECTOR, 'div[class="col-sm-4"] h3 a')
    PRICE_BASKET = (By.CSS_SELECTOR, 'div[class="col-sm-1"] p[class="price_color align-right"]')
    PRICE_STR = (By.CSS_SELECTOR, ' div.col-sm-6.product_main > p.price_color')

