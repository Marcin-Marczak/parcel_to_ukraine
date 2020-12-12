from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.driver.cookies_accept_button = (By.XPATH, "//a[@class='eupopup-closebutton']")
        self.parcel_weight_input = (By.XPATH, "//input[@name='parcelWeight']")
        self.homepage_submit_button = (By.XPATH, "//button[@class='btn btn-primary btn-block mt-3']")

    def open_homepage(self):
        self.driver.get("https://paczkadoukrainy.pl/")
        self.driver.find_element(*self.driver.cookies_accept_button).click()

    def enter_parcel_weight_homepage(self, weight):
        self.driver.find_element(*self.parcel_weight_input).send_keys(weight)
        self.driver.find_element(*self.homepage_submit_button).click()