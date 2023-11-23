from BaseApp import BasePage
from selenium.webdriver.common.by import By

class SeacrhLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, "loginEmail")
    LOCATOR_PASS_FIELD = (By.XPATH, "//input[@type='password']")
    LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, ".uk-button")
    LOCATOR_MAIN_TITLE = (By.TAG_NAME, "h3")
    LOCATOR_EMAIL_ERROR = (By.ID, "KEKEKEKEKEKKEKE")
    LOCATOR_EMPTY_EMAIL_ERROR = (By.ID, "emailFormatError")

class SearchHelper(BasePage):

    def login(self, login, password):
        email_field = self.find_element(SeacrhLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(login)
        pass_field = self.find_element(SeacrhLocators.LOCATOR_PASS_FIELD)
        pass_field.send_keys(password)
        return self.find_element(SeacrhLocators.LOCATOR_LOGIN_BUTTON,time=2).click()

    def enter_email(self, word):
        email_field = self.find_element(SeacrhLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(word)
        return email_field

    def enter_pass(self, word):
        pass_field = self.find_element(SeacrhLocators.LOCATOR_PASS_FIELD)
        pass_field.send_keys(word)
        return pass_field


    def click_on_the_button(self):
        return self.find_element(SeacrhLocators.LOCATOR_LOGIN_BUTTON,time=2).click()

    def check_main_title(self):
        main_title = self.find_element(SeacrhLocators.LOCATOR_MAIN_TITLE,time=2)
        return main_title

    def check_email_error_title(self):
        main_title = self.find_element(SeacrhLocators.LOCATOR_EMAIL_ERROR,time=2)
        return main_title

    def check_empty_email_error_title(self):
        main_title = self.find_element(SeacrhLocators.LOCATOR_EMPTY_EMAIL_ERROR,time=2)
        return main_title