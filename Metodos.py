import data
from selenium.webdriver.common.by import By


#Mejore la identacion de los localizadores y funcionaes para que interactuen mejor con las pruebas
class UrbanRoutesPage:

        from_field = (By.ID, 'from')
        to_field = (By.ID, 'to')
        mode_button = (By.CSS_SELECTOR, ".modes-container")
        ask_taxi = (By.CLASS_NAME, 'button.round')
        comfort_tarif = (By.CLASS_NAME, 'tcard-icon') #se cambio localizador
        phone = (By.CLASS_NAME, 'np - button')
        add_phone_number = (By.ID, 'phone')
        next_button = (By.CLASS_NAME, "button.full")
        confirmation_code = (By.CLASS_NAME, "button.full")
        add_code = (By.ID, "#code")
        payment_method = (By.CLASS_NAME, 'pp-button.filled')
        card = (By.CLASS_NAME, 'pp-plus-container')
        card_number = (By.CSS_SELECTOR, '#number.card-input')
        code_card = (By.XPATH, '//*[@id="code"]')
        card_space = (By.CSS_SELECTOR, '.plc')
        another_button_for_confirmation_credit_card = (By.CLASS_NAME, "pp-separator")
        add_credit_card = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[3]/button[1]') #no pude encontrar otro localizador :/
        close_card_button = (By.CLASS_NAME, "close-button.section-close")
        driver_message = (By.ID, 'comment')
        blanket_tissues = (By.CLASS_NAME, "slider.round")
        ice_cream = (By.CLASS_NAME, 'counter-value')
        reserve_button = (By.CLASS_NAME, "smart-button")

        def __init__(self, driver):
            self.driver = driver

        def get_from(self):
            return self.driver.find_element(*self.from_field).get_property('value')

        def get_to(self):
            return self.driver.find_element(self.from_field).get_property('value')
#Encontrar campos "desde" y "hasta"

        def set_from(self, from_address):
            self.driver.find_element(*self.from_field).send_keys(data.address_from)

#Desde
        def set_to(self, to_address):
            self.driver.find_element(*self.to_field).send_keys(data.address_to)

        def set_route(self, from_addres, to_address):
            self.set_from(from_addres)
            self.set_to(to_address)

#Hasta
        def click_ask_taxi(self):
            self.driver.find_element(*self.ask_taxi).click()

#Pedir taxi
        def select_comfort_tarif(self):
            self.driver.find_element(*self.comfort_tarif).click()

#Seleccionar confort
        def select_phone_number(self):
            self.driver.find_element(*self.phone).click()

#Seleccionar telefono
        def enter_phone_number(self, phone_number):
            self.driver.find_element(*self.add_phone_number).send_keys(data.phone_number)

#Agregar telefono
        def click_next(self):
            self.driver.find_element(*self.next_button).click()

#Continuar
        def enter_card_details(self, card_number, card_code):
            self.driver.find_element(*self.card_number).send_keys(data.card_number)
            self.driver.find_element(*self.code_card).send_keys(data.card_code)

#Agregar tarjeta
        def click_in_another_space_window_credit_card(self):
            self.driver.find_element(*self.another_button_for_confirmation_credit_card).click()

#Para habilitar la confirmacion
        def click_add_credit_card(self):
            self.driver.find_element(*self.add_credit_card).click()

#Terminar de agregar tarjeta
        def close_window_credit_card(self):
            self.driver.find_element(*self.close_card_button).click()

#Cerrar ventana de tarjeta
        def enter_driver_message(self, message):
            self.driver.find_element(*self.driver_message).send_keys(data.message_for_driver)

#Mensaje al conductor
        def blanket_tissues(self):
            self.driver.find_element(*self.blanket_tissues).click()

#Doble click en mantas y pañuelos
        def ice_cream(self):
            self.driver.find_element(*self.ice_cream).click().click()

#Helados
        def click_reserve(self):
            self.driver.find_element(*self.reserve_button).click()

#Reserva
