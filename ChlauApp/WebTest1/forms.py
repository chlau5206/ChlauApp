''' WebTest1/selenium_test.py
'''
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired

from .selenium_test import BasePage


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

