from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def find_result_text():
    driver = webdriver.Chrome()
    driver.maximize_window()
    input_data = 'perfect'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text').text
    print(result_text)


find_result_text()
