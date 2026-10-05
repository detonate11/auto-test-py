from selenium.webdriver.common.by import By
from locators import saucedemo_locators as loc
def test_clear_cart(driver):
    #проводим аторизацию
    driver.find_element(By.CSS_SELECTOR, loc.username).send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, loc.password).send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, loc.login).click()
    #добавляем в корзину
    driver.find_element(By.CSS_SELECTOR, loc.add).click()
    # переход в корзину
    driver.find_element(By.CSS_SELECTOR, loc.cart).click()
    #удаляем товар
    driver.find_element(By.CSS_SELECTOR, loc.remove).click()
    #проверка что товара нет в корзине
    products = driver.find_elements(By.CSS_SELECTOR, loc.remove)
    assert len(products) == 0, \
        "остались товары"
    #врзващаемся к выбору товара
    driver.find_element(By.CSS_SELECTOR, loc.continue_shopping).click()
    #проверяем что на странице выбора
    assert "inventory.html" in driver.current_url, \
        "не удалось вернуться "