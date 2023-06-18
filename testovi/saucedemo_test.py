from pages.login_page import HomePage
from pages.products_page import Products
from pages.checkout_page import Checkout

def test_login(driver):
    home_page = HomePage(driver)
    products_page = Products(driver)
    checkout_page = Checkout(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")
    assert home_page.isProductPageOpened() == "Products"
    products_page.addBackpackToCart()
    products_page.addOnesieToCart()
    products_page.openCart()
    assert products_page.getPageTitle() == "Your Cart"
    assert products_page.getProductTitle() =="Sauce Labs Backpack"
    assert products_page.getProductTitle2() == "Sauce Labs Onesie"
    products_page.clickCheckout()
    assert products_page.verifyCheckout() == "Checkout: Your Information"
    checkout_page.goToCheckout("Emina", "Mlivo", "70230")
    assert checkout_page.getCheckoutPageTitle() == "Checkout: Overview"
    checkout_page.clickFinish()
    assert checkout_page.getOrderConfirmationMessage() == "Thank you for your order!"
    checkout_page.openMenu()
    checkout_page.logout()
    assert home_page.isLoginPageOpened() == "Accepted usernames are:"


    



