import allure

from pages.base_page import BasePage
from pages.locators import RecoveryPasswordPageLocators


class RecoveryPage(BasePage):
    @allure.step('Дождаться загрузки страницы с восстановлением пароля')
    def loading_rec_password_page(self):
        return self.find_element_located(RecoveryPasswordPageLocators.HEADER_RECOVERY_PASSWORD)

    @allure.step('Ввести почту')
    def set_email(self, email):
        return self.find_element_located(RecoveryPasswordPageLocators.RECOVERY_EMAIL).send_keys(email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        return self.find_element_clickable(RecoveryPasswordPageLocators.RECOVERY_BUTTON)
