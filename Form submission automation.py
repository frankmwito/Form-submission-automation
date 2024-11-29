# Form submission automation using selenium in - https://demoqa.com/automation-practice-form

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import time 
import re

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)



try:
    driver.get("https://demoqa.com/automation-practice-form")
    
    Title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='text-center']"))).text
    print("The title is",Title)
    driver.maximize_window()
    
     # Faker data
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    phone_number = faker.phone_number()
    cleaned_phone_number = re.sub(r"\D", "", phone_number)[:10]
    address = faker.address()

    # Input Fields
    driver.find_element(By.ID, "firstName").send_keys(first_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(email)
    driver.execute_script(
        "arguments[0].click();", driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    )
    driver.find_element(By.ID, "userNumber").send_keys(cleaned_phone_number)

    # Date of Birth
    driver.find_element(By.ID, "dateOfBirthInput").click()
    Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_value("5")
    Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_value("1990")
    driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--015')]").click()
    
    # Subjects
    subjects_input = driver.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Computer Science")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'react-select-2-option')]"))
    )
    ActionChains(driver).move_to_element(
        driver.find_element(By.XPATH, "//div[contains(@id,'react-select-2-option-0')]")
    ).click().perform()

    # Hobbies Checkboxes
    driver.execute_script(
        "arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    )
    driver.execute_script(
        "arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    )
    driver.execute_script(
        "arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    )

    # File Upload
    file_path = r"C:\Users\Gaming 15\OneDrive\Pictures\New folder\images (1).jpeg"
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    # Address
    driver.find_element(By.ID, "currentAddress").send_keys(address)

    # State and City
    ActionChains(driver).move_to_element(driver.find_element(By.ID, "state")).click().perform()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Rajasthan')]"))
    ).click()

    ActionChains(driver).move_to_element(driver.find_element(By.ID, "city")).click().perform()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Jaipur')]"))
    ).click()

    # Submit Button
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "submit"))

finally:
    time.sleep(5)
    driver.quit()
    
    
    
    
    
    
    
         
    
    
    