from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        # Locators
        self.email_input = (By.ID, "new-email")
        self.password_input = (By.ID, "new-password")
        self.login_button = (By.XPATH, "//button[@type='submit' and text()='Login']")

    def open_login_page(self):
        self.driver.get("https://p2-admin-dash-qa.vercel.app/login")

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.email_input)
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()