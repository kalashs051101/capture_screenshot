from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def submit_to_google_form(form_data):
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform')

        # Wait for the form fields to be visible
        wait = WebDriverWait(driver, 10)

        name_field = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        name_field.send_keys(form_data.get('Name', ''))

        contact_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        contact_field.send_keys(form_data.get('Contact', ''))

        email_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        email_field.send_keys(form_data.get('Email', ''))

        address_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')))
        address_field.send_keys(form_data.get('Address', ''))

        pincode_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        pincode_field.send_keys(form_data.get('pincode', ''))

        dob_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')))
        dob_field.send_keys(form_data.get('Date_of_birth', ''))

        gender_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        gender_field.send_keys(form_data.get('Gender', ''))

        code_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        code_field.send_keys(form_data.get('code', ''))

        
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
        submit_button.screenshot('.\\test.png')
        submit_button.click()

        time.sleep(5)
        screenshot_path = '.\\confirmation_page.png'
        driver.save_screenshot(screenshot_path)

        driver.quit()

        return screenshot_path

    except Exception as e:
        print(f"Error: {e}")
        return None
