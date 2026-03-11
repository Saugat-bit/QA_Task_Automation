from utils.driver_setup import DriverSetup
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_customer_flow():
    email = "test_admin@yopmail.com"
    password = "Tester@123456"

    setup = DriverSetup()
    driver, wait = setup.get_driver()

    try:
        login_page = LoginPage(driver, wait)
        customer_page = CustomerPage(driver, wait)

        print("Opening login page...")
        login_page.open_login_page()

        print("Logging in...")
        login_page.login(email, password)

        print("Waiting for dashboard after login...")
        customers_menu = (By.XPATH, "//*[normalize-space()='Customers']")
        wait.until(EC.visibility_of_element_located(customers_menu))

        print("Opening Customers module...")
        customer_page.open_customers_module()

        print("Verifying Overview page...")
        assert customer_page.verify_overview_page(), "Overview page did not load."

        print("Fetching dashboard values...")
        dashboard_values = customer_page.get_dashboard_values()

        print("\nDashboard Values:")
        for key, value in dashboard_values.items():
            print(f"{key}: {value}")
            assert value != "", f"{key} is empty."

        print("\nOpening Customer Lists tab...")
        customer_page.open_customer_lists_tab()

        print("Verifying Customer List page...")
        assert customer_page.verify_customer_list_page(), "Customer list page did not load."

        print("Fetching first row data...")
        first_row_data = customer_page.get_first_row_data()

        print("\nFirst Row Customer Data:")
        for index, value in enumerate(first_row_data, start=1):
            print(f"Column {index}: {value}")
            assert value != "", f"First row column {index} is empty."

        print("\nCustomer Flow Test Passed Successfully")

    finally:
        setup.quit_driver()


if __name__ == "__main__":
    test_customer_flow()