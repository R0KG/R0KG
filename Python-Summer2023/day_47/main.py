from bs4 import BeautifulSoup
import requests
import lxml


header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5963.0 Safari/537.36"
}

response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=header)
soup = BeautifulSoup(response.content,"lxml")

print(soup.find(class_="a-size-large product-title-word-break").get_text())
print(soup.find(class_= "a-offscreen").get_text().strip())


