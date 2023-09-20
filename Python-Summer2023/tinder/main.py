from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
load_dotenv()
login_facebook = os.getenv("LOGIN")
pass_facebook = os.getenv("PASSWORD")

driver = webdriver.Chrome()
driver.get("https://tinder.onelink.me/9K8a/3d4abb81")
time.sleep(3)
# #Start tinder log_in
facebook_button = driver.find_element(By.XPATH,'//*[@id="u1031468980"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_button.click()
time.sleep(3)
main_window = driver.window_handles[0]
fc_window = driver.window_handles[1]
driver.switch_to.window(fc_window)
print(driver.title)
# cookies_access = driver.find_element(By.ID,"u_0_h_Y2")
# cookies_access.click()
fc_email = 

time.sleep(100)


