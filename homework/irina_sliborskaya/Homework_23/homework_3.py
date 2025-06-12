from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_submit_form(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    driver.find_element(By.ID, 'id_choose_language').click()
    selected_option = 'Python'
    driver.find_element(By.XPATH, f'//*[contains(text(), "{selected_option}")]').click()
    driver.find_element(By.ID, 'submit-id-submit').click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == selected_option


def test_check_text(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_btn = driver.find_element(By.XPATH, '//div[@id="start"]/button')
    start_btn.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'finish')))
    result = driver.find_element(By.XPATH, '//div[@id="finish"]/h4').text
    expected_text = 'Hello World!'
    assert result == expected_text
