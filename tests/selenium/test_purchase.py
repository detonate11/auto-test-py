from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import saucedemo_locators as loc
def test_success_purch(driver):
    #выполняем авторизацию
    driver.find_element(By.CSS_SELECTOR, loc.username).send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, loc.password).send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, loc.login).click()
    #добавление в корзину
    driver.find_element(By.CSS_SELECTOR, loc.add).click()
    #переход в корзину
    driver.find_element(By.CSS_SELECTOR, loc.cart).click()
    #оформление
    driver.find_element(By.CSS_SELECTOR, loc.checkout).click()
    #ввод данных
    driver.find_element(By.CSS_SELECTOR, loc.first_name).send_keys("georgy")
    driver.find_element(By.CSS_SELECTOR, loc.last_name).send_keys("markov")
    driver.find_element(By.CSS_SELECTOR, loc.postal_code).send_keys("111111")
    driver.find_element(By.CSS_SELECTOR, loc.continue_button).click()
    #добавляем ожидание перехода на страницу
        
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )
    print("URL после Continue:", driver.current_url)
    print("Текст страницы:", driver.find_element(By.TAG_NAME, "body").text)
    #завершение
    driver.find_element(By.CSS_SELECTOR, loc.finish).click()
    #проверка что оформление успешно
    message = driver.find_element(By.CSS_SELECTOR, loc.complete_header).text
    assert message == "Thank you for your order!"