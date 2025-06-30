from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://dodo.quantumnique.tech/login")

username=driver.find_element(By.CSS_SELECTOR,"input[name='username']")
username.send_keys("swetaraja2@gmail.com")

password=driver.find_element(By.CSS_SELECTOR,"input[type='password']")
password.send_keys("Student@123")

submit_button=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
submit_button.click()

time.sleep(7)
try:
    msd = driver.find_element(By.XPATH, "//*[contains(text(), 'Karpagam Assessments')]").text
    if "Karpagam Assessments " in msd:
        print("Successfully Logged In")
    else:
        print("Login Failed")
except:
    print("Failed")
driver.quit()