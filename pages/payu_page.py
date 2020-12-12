class PayUPage:
    def __init__(self, driver):
        self.driver = driver

    def get_payu_page_title(self):
        return self.driver.title