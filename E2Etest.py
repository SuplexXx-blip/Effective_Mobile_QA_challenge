from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

domain = 'https://www.saucedemo.com/'

browser.get(domain)

WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="login-button"]')))

browser.find_element(By.XPATH, '//input[@name="user-name"]').send_keys('standard_user')
browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('secret_sauce')
browser.find_element(By.XPATH, '//input[@value="Login"]').click()

WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Add to cart"]')))

browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.XPATH, '//button[@id="remove-sauce-labs-fleece-jacket"]'), "Remove"))
WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="1"]')))

browser.find_element(By.XPATH, '//a[@data-test="shopping-cart-link"]').click()

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.XPATH, '//div[@data-test="inventory-item-name"]'), "Sauce Labs Fleece Jacket"))

browser.find_element(By.XPATH, '//button[@id="checkout"]').click()

WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="first-name"]')))

browser.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('test')
browser.find_element(By.XPATH, '//input[@id="last-name"]').send_keys('test')
browser.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys('000000')
browser.find_element(By.XPATH, '//input[@id="continue"]').click()

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.XPATH, '//div[@data-test="inventory-item-name"]'), "Sauce Labs Fleece Jacket"))

browser.find_element(By.XPATH, '//button[@id="finish"]').click()

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.XPATH, '//h2[@data-test="complete-header"]'), "Thank you for your order!"))
WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="back-to-products"]')))

print("Тест прошёл! Покупка завершена успешно.")