from faker import Faker
import random


# Variables used as test data in end_to_end_test.py

weight_for_test = "12"

fake = Faker("pl")
sender_name_for_test = fake.first_name() + " " + fake.last_name()
sender_vat_for_test = random.randint(1000000000, 9999999999)
sender_postal_for_test = str(random.randint(11, 99)) + "-" + str(random.randint(111, 999))
sender_city_for_test = fake.city()
sender_street_for_test = fake.word() + "street"
sender_house_for_test = random.randint(1, 1000)
sender_flat_for_test = random.randint(1, 100)
sender_phone_for_test = random.randint(100000000, 999999999)
sender_email_for_test = fake.email()
fake = Faker("uk")
receiver_name_for_test = fake.name()
receiver_phone_for_test = random.randint(100000000, 999999999)
receiver_email_for_test = fake.email()

item1_name_for_test = 'Czekoladki'
item1_quantity_for_test = '2'
item1_weight_for_test = '10'
item1_value_for_test = '20'
item2_name_for_test = "Kubek"
item2_quantity_for_test = '1'
item2_weight_for_test = '2'
item2_value_for_test = '5'

summary_delivery_address = "Yevdokiivka, vul. Tsentralna,3"
summary_company_and_vat = sender_name_for_test + ' ' + str(sender_vat_for_test)

title_payu_page = "PayU"