from selenium.webdriver.common.by import By


class OrderSummaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.summary_texts = (By.XPATH, "//span[@class='calculator-summary__value ng-binding']")
        self.summary_parcel_details_texts = (By.XPATH, "//td[@class='ng-binding']")
        self.summary_order_price_text = (By.XPATH, "//span[@class='text-secondary ng-binding']")
        self.summary_submit_button = (By.XPATH, "//button[@class='btn btn-block btn-primary ng-scope']")

    def get_summary_delivery_address_text(self):
        return self.driver.find_elements(*self.summary_texts)[2].text

    def get_summary_sender_company_and_vat_text(self):
        return self.driver.find_elements(*self.summary_texts)[3].text

    def get_summary_item1_name_text(self):
        return self.driver.find_elements(*self.summary_parcel_details_texts)[1].text

    def get_summary_item2_name_text(self):
        return self.driver.find_elements(*self.summary_parcel_details_texts)[8].text

    def get_summary_order_price_text(self):
        return self.driver.find_element(*self.summary_order_price_text).text

    def submit_summary_page(self):
        self.driver.find_element(*self.summary_submit_button).click()