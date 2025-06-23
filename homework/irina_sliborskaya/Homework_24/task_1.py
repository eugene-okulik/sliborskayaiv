from argparse import Action
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_add_item(driver):
    driver.get('https://www.demoblaze.com/index.html')
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'card')))
    selected_item = 'Samsung galaxy s7'
    link = driver.find_element(By.XPATH, f'//a[@class="hrefch" and text()="{selected_item}"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'name')))
    driver.find_element(By.CSS_SELECTOR, "[onclick='addToCart(4)']").click()
    sleep(3)
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'cartur').click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'totalp')))
    item_in_cart = driver.find_element(By.XPATH, "//tbody[@id='tbodyid']/tr[1]/td[2]").text
    assert item_in_cart == selected_item
