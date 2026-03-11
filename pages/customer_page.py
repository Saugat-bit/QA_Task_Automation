from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CustomerPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.customers_menu = (By.XPATH, "//*[normalize-space()='Customers']")
        self.overview_tab = (By.XPATH, "//*[normalize-space()='Overview']")
        self.customer_lists_tab = (By.XPATH, "//*[normalize-space()='Customer Lists']")

        self.total_customers_value = (
            By.XPATH,
            "//*[normalize-space()='Total customers']/following::div[contains(@class,'text-h1')][1]"
        )
        self.total_active_customers_value = (
            By.XPATH,
            "//*[normalize-space()='Total active customers']/following::div[contains(@class,'text-h1')][1]"
        )
        self.total_inactive_customers_value = (
            By.XPATH,
            "//*[normalize-space()='Total inactive customers']/following::div[contains(@class,'text-h1')][1]"
        )
        self.total_under_warranty_value = (
            By.XPATH,
            "//*[normalize-space()='Total under warranty vehicles']/following::div[contains(@class,'text-h1')][1]"
        )

        self.customer_table = (By.XPATH, "//table")
        self.first_row = (By.XPATH, "//table/tbody/tr[1]")

    def open_customers_module(self):
        self.wait.until(
            EC.element_to_be_clickable(self.customers_menu)
        ).click()

    def verify_overview_page(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.overview_tab)
        ).is_displayed()

    def get_dashboard_values(self):
        total_customers = self.wait.until(
            EC.visibility_of_element_located(self.total_customers_value)
        ).text.strip()

        active_customers = self.wait.until(
            EC.visibility_of_element_located(self.total_active_customers_value)
        ).text.strip()

        inactive_customers = self.wait.until(
            EC.visibility_of_element_located(self.total_inactive_customers_value)
        ).text.strip()

        under_warranty = self.wait.until(
            EC.visibility_of_element_located(self.total_under_warranty_value)
        ).text.strip()

        return {
            "Total Customers": total_customers,
            "Active Customers": active_customers,
            "Inactive Customers": inactive_customers,
            "Under Warranty Vehicles": under_warranty
        }

    def open_customer_lists_tab(self):
        self.wait.until(
            EC.element_to_be_clickable(self.customer_lists_tab)
        ).click()

    def verify_customer_list_page(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.customer_table)
        ).is_displayed()

    def get_first_row_data(self):
        row = self.wait.until(
            EC.visibility_of_element_located(self.first_row)
        )
        cells = row.find_elements(By.TAG_NAME, "td")
        return [cell.text.strip() for cell in cells]