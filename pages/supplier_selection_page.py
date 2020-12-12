from selenium.webdriver.common.by import By


class SupplierSelectionPage:
    def __init__(self, driver):
        self.driver = driver

        self.supplier_selection_button = (By.XPATH, "//button[@class='btn font-weight-bold btn-primary height-fit-content ng-scope']")

    def selection_supplier(self):
        self.driver.find_elements(*self.supplier_selection_button)[5].click()