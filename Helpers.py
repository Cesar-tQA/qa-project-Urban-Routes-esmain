from selenium.webdriver.common.by import By

class UrbanRoutesPage:

    def __init__(self,driver):
        self.driver = driver

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    mode_button = (By.CSS_SELECTOR, ".modes-container")
    ask_taxi = (By.CLASS_NAME, 'button.round')
    comfort_tarif = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img') #By.ClASSNAME, 'tcard-icon')
    phone = (By.CLASS_NAME, 'np - button')
    add_phone_number = (By.ID, 'phone')
    next_button = (By.CLASS_NAME, "button.full")
    add_code = (By.ID, "#code")
    confirmation_code = (By.CLASS_NAME, "button.full")
    payment_method = (By.CLASS_NAME, 'pp-button.filled') #(By.CLASS_NAME "pp-text")
    card = (By.CLASS_NAME, 'pp-plus-container')
    card_number = (By.CSS_SELECTOR, '#number.card-input')
    code_card = (By.XPATH, '//*[@id="code"]')
    card_space = (By.CSS_SELECTOR, '.plc')
    add_credit_card = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_card_button = (By.CLASS_NAME, "close-button.section-close")
    driver_message = (By.ID, 'comment')
    blanket_tissues = (By.CLASS_NAME, "slider.round")
    ice_cream = (By.CLASS_NAME, 'counter-value')
    reserve_button = (By.CLASS_NAME, "smart-button")

