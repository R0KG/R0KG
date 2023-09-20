from selenium import webdriver
from selenium.webdriver.common.by import By
import time


LINK_SHEET = "https://docs.google.com/forms/d/e/1FAIpQLSddsUQgWKZrR_OZtdOU5iOt5l_6Ca4z8hSxyXUmO3geHrDT0Q/viewform?usp=sf_link"
LINK_RENT = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.65133894873047%2C%22east%22%3A-122.21531905126953%2C%22south%22%3A37.552434287743424%2C%22north%22%3A37.99747886057563%7D%2C%22mapZoom%22%3A11%2C%22usersSearchTerm%22%3A%22%22%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

driver = webdriver.Chrome()
driver.get(LINK_RENT)

time.sleep(5)

ul_element = driver.find_element(By.XPATH,'//*[@id="grid-search-results"]/ul')

li_elements = ul_element.find_elements(By.CSS_SELECTOR,'li')

for element in li_elements:
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 100);")
    temp_atr = element.get_attribute("data-test")
    if  temp_atr != "search-list-second-ad" and temp_atr != "search-list-first-ad":
        link = element.find_element(By.CSS_SELECTOR,"div a")
        print(link.get_attribute("href"))
    # link = element.find_element(By.TAG_NAME,"a")
    # print(link.get_attribute("href"))
        
    
driver.quit()
