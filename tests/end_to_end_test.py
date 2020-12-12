from tests.data_used_in_tests import *
import pytest
import time
from pages.home_page import HomePage
from pages.supplier_selection_page import SupplierSelectionPage
from pages.order_details_page import OrderDetailsPage
from pages.order_summary_page import OrderSummaryPage
from pages.payu_page import PayUPage


@pytest.mark.usefixtures("setup")
class TestEndToEndOrder:

    def test_01_end_to_end_order_process(self):
        home_page = HomePage(self.driver)
        home_page.open_homepage()
        home_page.enter_parcel_weight_homepage(weight_for_test)
        self.driver.implicitly_wait(10)

        supplier_selection_page = SupplierSelectionPage(self.driver)
        supplier_selection_page.selection_supplier()
        self.driver.implicitly_wait(10)

        order_details_page = OrderDetailsPage(self.driver)
        order_price_for_test = order_details_page.get_total_order_price_text()
        time.sleep(2)
        order_details_page.sender_type_complete()
        time.sleep(3)
        order_details_page.delivery_type_complete()
        time.sleep(3)
        order_details_page.sender_complete(sender_name_for_test, sender_vat_for_test, sender_postal_for_test, sender_city_for_test, sender_street_for_test, sender_house_for_test, sender_flat_for_test, sender_phone_for_test, sender_email_for_test)
        order_details_page.receiver_complete(receiver_name_for_test, receiver_phone_for_test, receiver_email_for_test)
        order_details_page.declaration_complete(item1_name_for_test, item1_quantity_for_test, item1_weight_for_test, item1_value_for_test, item2_name_for_test, item2_quantity_for_test, item2_weight_for_test, item2_value_for_test)
        order_details_page.mark_forms()
        order_details_page.submit_details_page()
        self.driver.implicitly_wait(10)

        order_summary_page = OrderSummaryPage(self.driver)
        assert summary_delivery_address == order_summary_page.get_summary_delivery_address_text()
        assert summary_company_and_vat == order_summary_page.get_summary_sender_company_and_vat_text()
        assert item1_name_for_test == order_summary_page.get_summary_item1_name_text()
        assert item2_name_for_test == order_summary_page.get_summary_item2_name_text()
        assert order_price_for_test == order_summary_page.get_summary_order_price_text()
        order_summary_page.submit_summary_page()
        self.driver.implicitly_wait(10)

        payu_page = PayUPage(self.driver)
        time.sleep(5)
        assert title_payu_page == payu_page.get_payu_page_title()