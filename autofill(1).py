from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome()

url = "https://forms.office.com/r/pdJVwcVnZJ"
for i in range(56):
    driver.get(url)
    driver.implicitly_wait(200)
    # answers = driver.find_elements(By.CSS_SELECTOR, '.css-44')
    # answers = driver.find_elements(By.CSS_SELECTOR, '.css-43')
    # answers = driver.find_elements(By.CSS_SELECTOR, '.css-261')
    answers = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="questionItem"]')

    for answer in answers:
        ans = answer.find_elements(By.CSS_SELECTOR, 'input')
        co = random.choice(ans)
        co.click()
    driver.find_elements(By.TAG_NAME, 'button')[-1].click()
    # submit_button = driver.find_elements(By.CSS_SELECTOR,'.css-184')[-1].click()

    # answers = driver.find_elements_by_css_selector('.office-form-question-content')
    # for answer in answers:
    #     ans = answer.find_elements_by_css_selector('input')
    #     if not ans:
    #         continue
    #     co = random.choice(ans)
    #     co.click()
    # submit_button = driver.find_elements(By.CSS_SELECTOR, "button")
    # button = submit_button[-1]
    # button.click()
    # driver.implicitly_wait(30)
