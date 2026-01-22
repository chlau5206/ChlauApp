""" WebTest1/selenium_test.py 

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")

    # Actions
    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

def test_login():
    # Set up the WebDriver
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    # Test with the Page Object Model
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()

    # Close the browser
    driver.quit()