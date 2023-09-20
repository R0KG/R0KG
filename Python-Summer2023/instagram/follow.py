from selenium import webdriver
from selenium.webdriver.common.by import By
import time
USERNAME = "r0manj"
PASSWORD = "1Merkulov"
ACCOUNT_NAME = "sciencemagazine"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        time.sleep(3)
    def log_in(self):
        butt = self.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        butt.click()
        time.sleep(3)
        login_inp = self.driver.find_element(By.NAME,"username")
        login_inp.send_keys(USERNAME)
        time.sleep(1.5)
        pass_inp = self.driver.find_element(By.NAME,"password")
        pass_inp.send_keys(PASSWORD)

        anmelden_button = self.driver.find_element(By.CSS_SELECTOR,'[type="submit"]')
        anmelden_button.click()
        time.sleep(3)
        # inf_speichern_element = self.driver.find_element(By.CSS_SELECTOR, "section dev button")
        # inf_speichern_element.click()
        time.sleep(5)
        suchen_inp = self.driver.find_element(By.CSS_SELECTOR,'[placeholder="Suchen"]').click()
        suchen_inp.send_keys(ACCOUNT_NAME)
        time.sleep(3)
        account_click = self.driver.find_element(By.LINK_TEXT,"sciencemagazine")
        account_click.click()
        time.sleep(3)
        #jetzt_nicht_button = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_6H"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        #jetzt_nicht_button.click()
        
        
        
        time.sleep(300000)
        
