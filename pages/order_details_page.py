from selenium.webdriver.common.by import By
import time


class OrderDetailsPage:
    def __init__(self, driver):
        self.driver = driver

        self.total_price_text = (By.XPATH, "//span[@class='selected-carrier__price-value ng-binding ng-scope']")

        self.sender_type_radio = (By.XPATH, "//label[@for='COMPANY']")

        self.delivery_type_radio = (By.XPATH, "//label[@for='pickupPoint']")
        self.delivery_point_radio = (By.XPATH, "//label[@for='NOVA_POSHTA']")
        self.delivery_address_open_field = (By.XPATH, "//div[@class='selectize-input']")
        self.delivery_address_input = (By.XPATH, "//span[text()='Yevdokiivka, vul. Tsentralna,3']")

        self.sender_company_name_input = (By.ID, "senderCompanyName")
        self.sender_vat_input = (By.ID, "senderCompanyVatId")
        self.sender_postal_code_input = (By.ID, "senderPostalCode")
        self.sender_city_input = (By.ID, "senderCity")
        self.sender_street_input = (By.ID, "senderStreet")
        self.sender_house_number_input = (By.ID, "senderHouseNumber")
        self.sender_flat_number_input = (By.ID, "senderFlatNumber")
        self.sender_phone_input = (By.ID, "senderPhone")
        self.sender_email_input = (By.ID, "senderEmail")

        self.receiver_name_input = (By.ID, "receiverName")
        self.receiver_phone_input = (By.ID, "receiverPhone")
        self.receiver_email_input = (By.ID, "receiverEmail")

        self.declaration_position_add_button = (By.XPATH, "//button[text()= 'Dodaj kolejną pozycję']")

        self.parcel_description_input = (By.XPATH, "//input[@id='parcelItemDescription']")
        self.parcel_quantity_input = (By.XPATH, "//input[@id='parcelItemQuantity']")
        self.parcel_weight_input = (By.XPATH, "//input[@id='parcelItemWeight']")
        self.parcel_value_input = (By.XPATH, "//input[@id='parcelItemValueClientCurrency']")

        self.form_regulation_1_radio = (By.XPATH, "//label[@for='orderFormRegulation']")
        self.form_regulation_prohibited_goods_radio = (By.XPATH, "//label[@for='orderProhibitedGoods']")
        self.form_regulation_2_radio = (By.XPATH, "//label[@for='orderFormRegulation2']")

        self.order_details_next_step_button = (By.ID, "btn_next_step")

    def get_total_order_price_text(self):
        return self.driver.find_element(*self.total_price_text).text.replace(",", ".")

    def sender_type_complete(self):
        self.driver.find_element(*self.sender_type_radio).click()

    def delivery_type_complete(self):
        self.driver.find_element(*self.delivery_type_radio).click()
        time.sleep(5)
        self.driver.find_element(*self.delivery_point_radio).click()
        time.sleep(5)
        self.driver.find_element(*self.delivery_address_open_field).click()
        self.driver.find_element(*self.delivery_address_input).click()

    def sender_complete(self, sender_name, sender_vat, sender_postal, sender_city, sender_street, sender_house, sender_flat, sender_phone, sender_email):
        self.driver.find_element(*self.sender_company_name_input).send_keys(sender_name)
        self.driver.find_element(*self.sender_vat_input).send_keys(sender_vat)
        self.driver.find_element(*self.sender_postal_code_input).send_keys(sender_postal)
        self.driver.find_element(*self.sender_city_input).send_keys(sender_city)
        self.driver.find_element(*self.sender_street_input).send_keys(sender_street)
        self.driver.find_element(*self.sender_house_number_input).send_keys(sender_house)
        self.driver.find_element(*self.sender_flat_number_input).send_keys(sender_flat)
        self.driver.find_element(*self.sender_phone_input).send_keys(sender_phone)
        self.driver.find_element(*self.sender_email_input).send_keys(sender_email)

    def receiver_complete(self, receiver_name, receiver_phone, receiver_email):
        self.driver.find_element(*self.receiver_name_input).send_keys(receiver_name)
        self.driver.find_element(*self.receiver_phone_input).send_keys(receiver_phone)
        self.driver.find_element(*self.receiver_email_input).send_keys(receiver_email)

    def declaration_complete(self, item1_name, item1_quantity, item1_weight, item1_value, item2_name, item2_quantity, item2_weight, item2_value):
        self.driver.find_element(*self.declaration_position_add_button).click()
        self.driver.find_elements(*self.parcel_description_input)[0].send_keys(item1_name)
        self.driver.find_elements(*self.parcel_quantity_input)[0].send_keys(item1_quantity)
        self.driver.find_elements(*self.parcel_weight_input)[0].send_keys(item1_weight)
        self.driver.find_elements(*self.parcel_value_input)[0].send_keys(item1_value)

        self.driver.find_elements(*self.parcel_description_input)[1].send_keys(item2_name)
        self.driver.find_elements(*self.parcel_quantity_input)[1].send_keys(item2_quantity)
        self.driver.find_elements(*self.parcel_weight_input)[1].send_keys(item2_weight)
        self.driver.find_elements(*self.parcel_value_input)[1].send_keys(item2_value)

    def mark_forms(self):
        self.driver.find_element(*self.form_regulation_1_radio).click()
        self.driver.find_element(*self.form_regulation_prohibited_goods_radio).click()
        self.driver.find_element(*self.form_regulation_2_radio).click()

    def submit_details_page(self):
        self.driver.find_element(*self.order_details_next_step_button).click()