# Form submission automation using selenium in - https://demoqa.com/automation-practice-form

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
    
    # Use faker to obtain test data for test automation
    faker = Faker()
    first_name = faker.first_name_male()
    second_name = faker.last_name_male()
    email = faker.email()
    phone_number = faker.phone_number()
    cleaned_phone_number = re.sub(r'\D','',phone_number)
    address = faker.address()
    
    time.sleep(2)
    
    First_Name = driver.find_element(By.ID,"firstName")
    First_Name.send_keys(first_name)
    
    time.sleep(2)
    
    Last_Name = driver.find_element(By.ID,"lastName")
    Last_Name.send_keys(second_name)
    
    time.sleep(2)
    
    input_email = driver.find_element(By.CSS_SELECTOR,"#userEmail")
    input_email.send_keys(email)
    
    time.sleep(2)
    

    gender_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    driver.execute_script("arguments[0].click();", gender_radio)
        
    time.sleep(2)  
        
    
    Phone_number = driver.find_element(By.XPATH,"//input[@id='userNumber']")
    Phone_number.send_keys(cleaned_phone_number)
    
    time.sleep(2)
    
  # Date of Birth
    date_input = driver.find_element(By.ID, "dateOfBirthInput")
    date_input.click()
    month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month.select_by_value("5")
    year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year.select_by_value("2024")
    driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--015')]").click()
    
    time.sleep(2)
            
  # Subjects
    driver.find_element(By.ID, "subjectsInput").send_keys("Computer Science")
    autocomplete = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
    print(len(autocomplete))
    for result in autocomplete:
        if result.text == "Computer science":
            result.click()
            break
    
    # Checkboxes
    time.sleep(2)
    
    # Checkbox1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"label[for='hobbies-checkbox-1']")))
    # Checkbox1.click()
    
    # time.sleep(2)
     
    # Checkbox2 = driver.find_element(By.CSS_SELECTOR,"label[for='hobbies-checkbox-2']")
    # Checkbox2.click()
    
    # time.sleep(2)
    
    # Checkbox3 = driver.find_element(By.CSS_SELECTOR,"label[for='hobbies-checkbox-3']")
    # Checkbox3.click()
    
    # Photo locator and input address
    file_input = driver.find_element(By.XPATH,"//input[@id='uploadPicture']")
    
    time.sleep(2)
    
    file_path = "C:/Users/Gaming 15/OneDrive/Pictures/New folder/images (1).jpeg"
    
    time.sleep(2)
    
    file_input.send_keys(file_path)
    # address locator and input
    current_address = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
    current_address.send_keys(address)
    
    time.sleep(2)

    # Select class for the dropdown button with autosuggestion
    # select State
 # State and City
    state = driver.find_element(By.ID, "state")
    state.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Rajasthan')]"))).click()

    city = driver.find_element(By.ID, "city")
    city.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Jaipur')]"))).click()


    time.sleep(2)
    # Submit button
    
    submit_button = driver.find_element(By.CSS_SELECTOR,"#submit")
    submit_button.click()
    
finally:
    time.sleep(10)
    
    driver.quit()
    
    
    
    
    
    
    
         
    
    
    