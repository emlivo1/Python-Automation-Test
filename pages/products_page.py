from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Products:

    def __init__(self, driver):
        self.test_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def addBackpackToCart(self):
        addBackpackBtn = self.test_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        addBackpackBtn.click()
        

    def addOnesieToCart(self):
        addOnesieBtn = self.test_driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        addOnesieBtn.click()
    
    def openCart(self):
        cartBtn = self.test_driver.find_element(By.XPATH, "//a[@class=\"shopping_cart_link\"]")
        cartBtn.click()
    
    def getPageTitle(self):
        titleText = (By.XPATH, "//span[text()=\"Your Cart\"]")
        waitTitleText = self.wait.until(EC.visibility_of_element_located(titleText))
        titleText = waitTitleText.text
        return titleText
    
    def getProductTitle(self):
        productTitle = (By.XPATH, "//div[text()=\"Sauce Labs Backpack\"]")
        waitProductTitle = self.wait.until(EC.element_to_be_clickable(productTitle))
        productTitlesText = waitProductTitle.text
        return productTitlesText
    
    def getProductTitle2(self):
        
        productTitle = (By.XPATH, "//div[text()=\"Sauce Labs Onesie\"]")
        waitProductTitle = self.wait.until(EC.element_to_be_clickable(productTitle))
        productTitleText = waitProductTitle.text
        return productTitleText

    def clickCheckout(self):
        checkoutBtn = self.test_driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
    
    def verifyCheckout(self):
        title = (By.XPATH, "//span[text()=\"Checkout: Your Information\"]")
        waitTitle = self.wait.until(EC.visibility_of_element_located(title))
        text = waitTitle.text
        return text