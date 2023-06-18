from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout = 60)

    def goToCheckout(self, firstName, lastName, postalCode):
        nameField = (By.ID, "first-name")
        waitName = self.wait.until(EC.element_to_be_clickable(nameField))
        waitName.click()
        waitName.clear()
        waitName.send_keys(firstName)

        surnameField = (By.ID, "last-name")
        waitSurname = self.wait.until(EC.element_to_be_clickable(surnameField))
        waitSurname.click()
        waitSurname.clear()
        waitSurname.send_keys(lastName)

        postalCodeField = (By.ID, "postal-code")
        waitPostalCode = self.wait.until(EC.element_to_be_clickable(postalCodeField))
        waitPostalCode.click()
        waitPostalCode.clear()
        waitPostalCode.send_keys(postalCode)

        continueBtn = self.driver.find_element(By.ID, "continue")
        continueBtn.click()
    
    def getCheckoutPageTitle(self):
        titleTextField = (By.XPATH, "//span[text()=\"Checkout: Overview\"]")
        waitTitleText = self.wait.until(EC.visibility_of_element_located(titleTextField))
        titleText = waitTitleText.text
        return titleText
    
    def clickFinish(self):
        finishBtn = self.driver.find_element(By.ID, "finish")
        finishBtn.click()
    
    def getOrderConfirmationMessage(self):
        confirmationMessage = (By.XPATH, "//h2[text()=\"Thank you for your order!\"]")
        waitConfirmationMessage = self.wait.until(EC.visibility_of_element_located(confirmationMessage))
        messageText = waitConfirmationMessage.text
        return messageText
    
    def openMenu(self):
        menuButton = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menuButton.click()
    
    def logout(self):
        logout = (By.ID, "logout_sidebar_link")
        logoutBtn = self.wait.until(EC.element_to_be_clickable(logout))
        logoutBtn.click()

