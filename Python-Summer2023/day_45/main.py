import requests
from bs4 import BeautifulSoup

# response = requests.get(url="https://news.ycombinator.com/")
# bloomberg_webpage = response.text

# soup = BeautifulSoup(bloomberg_webpage,"html.parser")
# texts = soup.select(".athing")
# scores = soup.select(".score")
# scores_int = [int(score.get_text().split("points")[0]) for score in scores]
# max_index = scores_int.index(max(scores_int))
# texts_list = [ text.get_text() for text in texts]
# print(texts_list[5])


response = requests.get(url="https://www.timeout.com/film/best-movies-of-all-time").text

soup = BeautifulSoup(response,"html.parser")
movies_names = soup.select("._h3_cuogz_1")
with open("./movies.txt","w") as file:
    for movie in movies_names:
        temp = f"{movie.getText()}\n"
        file.write(temp)











# with open(file= "website.html", encoding= "UTF-8") as data:
#     text = data.read()
    
# soup = BeautifulSoup(text, "html.parser")
# print(soup.select_one("li a"))
