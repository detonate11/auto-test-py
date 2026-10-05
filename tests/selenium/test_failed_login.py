import allure

from selenium.webdriver.common.by import By
from locators import saucedemo_locators as loc

@allure.suite("SauceDemo")
class TestfailLogin:
    @allure.title("неуспешная авторизация")
    @allure.label("owner", "Markov")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_failed_login(self, driver):
#ввод неверных даннызх
        with allure.step("не корректный вход"):
            driver.find_element(By.CSS_SELECTOR, loc.username).send_keys("wrong_user")
            driver.find_element(By.CSS_SELECTOR, loc.password).send_keys("wrong_password")
            driver.find_element(By.CSS_SELECTOR, loc.login).click()
    #сообщение об ошибке
        with allure.step("error message"):
            error_message = driver.find_element(By.CSS_SELECTOR, loc.error).text
    #проверяем
        with allure.step("checkoing"):
            assert "Username and password do not match" in error_message, \
                f"некорректная проверка: {error_message}"