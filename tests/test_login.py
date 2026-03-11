from utils.driver_setup import DriverSetup
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login():

    email = "test_admin@yopmail.com"
    password = "Tester@123456"

    setup = DriverSetup()
    driver, wait = setup.get_driver()

    try:
        login_page = LoginPage(driver, wait)

        print("Opening login page...")
        login_page.open_login_page()

        print("Entering login credentials...")
        login_page.login(email, password)

        print("Checking if login successful...")

        customers_menu = (By.XPATH, "//*[normalize-space()='Customers']")
        wait.until(EC.visibility_of_element_located(customers_menu))

        current_url = driver.current_url
        print("Current URL:", current_url)

        assert "/profile" in current_url or "login" not in current_url.lower(), "Login failed."

        print("Login Test Passed Successfully")

    finally:
        setup.quit_driver()


if __name__ == "__main__":
    test_login()