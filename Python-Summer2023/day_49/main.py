from selenium import webdriver
import time
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3691314630&distance=25&f_AL=true&geoId=107144641&keywords=python/")
time.sleep(2.5)
#Log in
log_in_button = driver.find_element(By.CLASS_NAME,"nav__button-secondary")
log_in_button.click()
username_window = driver.find_element(By.ID,"username")
username_window.send_keys("int1994019@gmail.com")
password_window = driver.find_element(By.ID,"password")
password_window.send_keys("KG0065187r!")
log_on_butt_2 = driver.find_element(By.CLASS_NAME,"btn__primary--large")
log_on_butt_2.click()

#Subscire to a list of jobs
time.sleep(2)
ul_element = driver.find_element(By.CLASS_NAME,"scaffold-layout__list-container")
list_jobs = ul_element.find_elements(By.TAG_NAME,"li")

for job in list_jobs:
    job.click()
    time.sleep(2)
    temp_butt = driver.find_element(By.CLASS_NAME,"jobs-save-button")
    temp_butt.click()
    time.sleep(1)

time.sleep(500)
