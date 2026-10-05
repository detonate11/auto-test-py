from selenium.webdriver.common.by import By
from locators import saucedemo_locators as loc
def test_failed_login(driver):
#ввод неверных даннызх
    driver.find_element(By.CSS_SELECTOR, loc.username).send_keys("wrong_user")
    driver.find_element(By.CSS_SELECTOR, loc.password).send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, loc.login).click()
    #сообщение об ошибке
    error_message = driver.find_element(By.CSS_SELECTOR, loc.error).text
    #проверяем
    assert "Username and password do not match" in error_message, \
    f"некорректная проверка: {error_message}"