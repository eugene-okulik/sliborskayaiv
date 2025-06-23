from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_compare_item(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@role="dialog"]')))
    driver.find_element(By.XPATH, '//button[@aria-label="Consent"]').click()
    selected_item = driver.find_element(By.XPATH,
                                        '//li[contains(@class, "product-item")]//a[@class="product-item-link"]')
    selected_item_name = selected_item.text.strip()
    add_to_compare = driver.find_element(By.XPATH, '//a[@class="action tocompare"]')
    ActionChains(driver).move_to_element(selected_item).click(add_to_compare).perform()
    (WebDriverWait(driver, 10).
     until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby="block-compare-heading"]'))))
    product_link = driver.find_element(By.XPATH,
                                       "//ol[@id='compare-items']//a[contains(@class, 'product-item-link')]")
    item_in_compare_name = product_link.text.strip()
    assert selected_item_name == item_in_compare_name
