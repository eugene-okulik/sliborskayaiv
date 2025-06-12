from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def submit_form():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form')
    first_name_field = driver.find_element(By.ID, 'firstName')
    last_name_field = driver.find_element(By.ID, 'lastName')
    email_field = driver.find_element(By.ID, 'userEmail')
    female_gender_option = driver.find_elements(By.CLASS_NAME, 'custom-control')
    mobile_number = driver.find_element(By.ID, 'userNumber')
    hobbies_checkbox_1 = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    address_field = driver.find_element(By.ID, 'currentAddress')
    state_selector = driver.find_element(By.XPATH, "//div[contains(text(), 'Select State')]")
    city_selector = driver.find_element(By.ID, 'city')
    submit_btn = driver.find_element(By.ID, 'submit')

    first_name_field.send_keys('Irina')
    last_name_field.send_keys('Test')
    email_field.send_keys('test@test.co')
    female_gender_option[1].click()
    mobile_number.send_keys('1234567890')
    hobbies_checkbox_1.click()
    address_field.send_keys('New Street, 123, 05-358, Warsaw, Poland')
    state_selector.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Haryana']"))).click()
    city_selector.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Karnal']"))).click()
    submit_btn.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

    for row in rows:
        data = row.find_elements(By.TAG_NAME, 'td')
        if len(data) == 2:
            label = data[0].text
            values = data[1].text
            print(f'{label}: {values}')


submit_form()
