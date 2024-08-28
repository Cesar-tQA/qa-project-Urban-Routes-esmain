import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Metodos import UrbanRoutesPage
from Helpers import phone_code

#Pase la informacion completa de main a este documento y elimine el archivo main.


class Test_Urban_Routes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        set_from = routes_page.set_from(data.address_from)
        set_to = routes_page.set_to(data.address_to)
        routes_page.set_route(set_from, set_to)
        WebDriverWait(self.driver, 1).until(
            expected_conditions.text_to_be_present_in_element_value((By.ID, 'from'), data.address_from)
        )
        WebDriverWait(self.driver, 1).until(
            expected_conditions.text_to_be_present_in_element_value((By.ID, 'to'), data.address_to)
        )
        assert set_from == data.address_from, f"Error: 'from' no se estableció correctamente. Se esperaba {data.address_from}, pero se obtuvo {set_from}"
        assert set_to == data.address_to, f"Error: 'to' no se estableció correctamente. Se esperaba {data.address_to}, pero se obtuvo {set_to}"

    def test_ask_for_taxi(self):
        ask_taxi_button = self.driver.find_element(UrbanRoutesPage.ask_taxi)
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi)
                                            )
        ask_taxi_button.click()
        assert self.test_ask_for_taxi()

    def test_select_comfort_tarif(self):
        comfort_tarif_button = self.driver.find_element(UrbanRoutesPage.comfort_tarif)
        comfort_tarif_button.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.add_phone_number)
        )
        assert comfort_tarif_button.is_selected(), "Error: La tarifa confort no fue seleccionada correctamente."

    def test_add_phone_number(self):
        phone_button = self.driver.find_element(UrbanRoutesPage.phone)
        phone_number = self.driver.find_element(UrbanRoutesPage.add_phone_number)
        button_next = self.driver.find_element(UrbanRoutesPage.next_button)
        confirmation_code = self.driver.find_element(phone_code)
        confirmation_button = self.driver.find_element(UrbanRoutesPage.confirmation_code)
        phone_button.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.add_phone_number)
        )
        phone_number.click()
        phone_number.send_keys(data.phone_number)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.confirmation_code)
        )
        confirmation_button.send_keys(confirmation_code)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.confirmation_code)
        )
        button_next.click()
        displayed_phone_number = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'np-text'))
        ).text
        assert displayed_phone_number == data.phone_number, "Error: El número de teléfono no se muestra correctamente en el formulario."

    def test_add_method_payment(self):
        pay_method_button = self.driver.find_element(UrbanRoutesPage.payment_method)
        add_card_button = self.driver.find_element(UrbanRoutesPage.card)
        number_of_card = self.driver.find_element(UrbanRoutesPage.card_number)
        cvv_card = self.driver.find_element(UrbanRoutesPage.code_card)
        another_button = self.driver.find_element(UrbanRoutesPage.another_button_for_confirmation_credit_card)
        pay_method_button.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.card)
        )
        add_card_button.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.card_number))
        number_of_card.send_keys(data.card_number)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.code_card)
        )
        cvv_card.click()
        cvv_card.send_keys(data.card_code)
        another_button.click()
        pp_value_text = self.driver.find_element(By.CLASS_NAME, 'pp-value-text')
        assert pp_value_text.text == 'Tarjeta', "Error: El texto en el campo de validación no es 'Tarjeta'."
        assert number_of_card.get_attribute(
            'value') == data.card_number, "Error: El número de tarjeta no fue ingresado correctamente."
        assert cvv_card.get_attribute(
            'value') == data.card_code, "Error: El código de tarjeta no fue ingresado correctamente."

    def test_select_blanket_tissues(self):
        blanket_tissues_button = self.driver.find_element(UrbanRoutesPage.blanket_tissues)
        blanket_tissues_button.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.blanket_tissues)
        )
        assert blanket_tissues_button.is_selected(), "Error: la opcion de mantas y pañuelos no fueron seleccionadas correctamente"

    def test_ice_cream_double_click(self):
        ice_cream_button = self.driver.find_element(UrbanRoutesPage.ice_cream)
        counter_value = self.driver.find_element(UrbanRoutesPage.ice_cream)
        for _ in range(2):
            ice_cream_button.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.ice_cream)
        )
        assert counter_value.text == '2', "Error: el número de helados seleccionados no es 2."

    def test_reserve(self):
        button_of_reserve = self.driver.find_element(UrbanRoutesPage.reserve_button)
        button_of_reserve.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'order-header-title'))
        )
        assert self.driver.find_element(By.CLASS_NAME,
                                        'order-header-title').is_displayed(), "Error: El modal de reserva no se mostró."

    """No estoy completamente seguro si escribi correctamente el verificador para la sugerencia, pregunte a algunos compañeros al
    respecto y me comentaron que podria estructurarse de la manera en la que lo escribi, sin embargo, no entiendo completamente como
    una clase que no esta establecida en los localizadores puede verificar si el modal arroja la informacion esperada. Espero que 
    el cambio escrito sea el esperado"""

    def teardown_class(cls):
        cls.driver.quit()
