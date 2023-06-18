from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self.test_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.test_driver.get("https://www.saucedemo.com/")
        self.test_driver.maximize_window()
    
    def login(self, username, password):
        input_username = (By.ID, "user-name")
        wait_username_input = self.wait.until(EC.element_to_be_clickable(input_username))
        wait_username_input.click()
        wait_username_input.clear()
        wait_username_input.send_keys(username)

        password_field = self.test_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_btn = self.test_driver.find_element(By.ID, "login-button")
        login_btn.click()
    
    def isProductPageOpened(self):
        page_title = (By.XPATH, "//span[text()=\"Products\"]")
        wait_page_title = self.wait.until(EC.visibility_of_element_located(page_title))
        page_title = wait_page_title.text
        return page_title
    
    def isLoginPageOpened(self):
        loginPage = (By.XPATH, "//h4[text()=\"Accepted usernames are:\"]")
        waitLogin = self.wait.until(EC.visibility_of_element_located(loginPage))
        loginPageText = waitLogin.text
        return loginPageText



