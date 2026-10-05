import allure
from selenium.webdriver.common.by import By
from locators import saucedemo_locators as loc

@allure.suite("SauceDemo")
class TestClearCart:
    @allure.title("очистка корзины")
    @allure.label("owner", "Markov")
    @allure.severity(allure.severity_level.NORMAL)

    def test_clear_cart(self, driver):
    #проводим аторизацию
        with allure.step("authorisation"):
            driver.find_element(By.CSS_SELECTOR, loc.username).send_keys("standard_user")
            driver.find_element(By.CSS_SELECTOR, loc.password).send_keys("secret_sauce")
            driver.find_element(By.CSS_SELECTOR, loc.login).click()
    #добавляем в корзину
        with allure.step("add to cart"):
            driver.find_element(By.CSS_SELECTOR, loc.add).click()
    # переход в корзину
        with allure.step("move to cart"):
            driver.find_element(By.CSS_SELECTOR, loc.cart).click()
    #удаляем товар
        with allure.step("remove"):
            driver.find_element(By.CSS_SELECTOR, loc.remove).click()
    #проверка что товара нет в корзине
        with allure.step("check emty cart"):
            products = driver.find_elements(By.CSS_SELECTOR, loc.remove)
            assert len(products) == 0, \
                "остались товары"
    #врзващаемся к выбору товара
        with allure.step("back"):
            driver.find_element(By.CSS_SELECTOR, loc.continue_shopping).click()
    #проверяем что на странице выбора
        with allure.step("check current page"):
            assert "inventory.html" in driver.current_url, \
                "не удалось вернуться "