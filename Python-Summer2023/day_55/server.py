from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0,9)
LINK = "https://media3.giphy.com/media/4JVTF9zR9BicshFAb7/giphy.gif?cid=ecf05e47kp6tv6vl016b4gn6dz74wupfs6fe4yt1shjov51g&ep=v1_gifs_search&rid=giphy.gif&ct=g"

@app.route("/")
def start():
    return "<h1>Guess a number between 0 and 9</h1>" \
        f'<img src ={LINK}>'

@app.route("/<int:number>")
def check_result(number):
    if number == random_num:
        return "<h1>You found me!!!</h1>" \
            '<img src ="https://media4.giphy.com/media/Y4pAQv58ETJgRwoLxj/giphy.gif?cid=ecf05e47cge05knugssaspxg76reaz3urvtdqys4qram2sfn&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    elif number > random_num:
        return "<h1>Too high!!!</h1>" \
            '<img src ="https://www.reddit.com/r/Eyebleach/comments/6l8yik/puppy_rides_the_bike/">'
    elif number < random_num:
        return "<h1>Too low!!!</h1>" \
            '<img src ="https://media0.giphy.com/media/3o8doVAxrMjXbIHaU0/giphy.gif?cid=ecf05e47cge05knugssaspxg76reaz3urvtdqys4qram2sfn&ep=v1_gifs_search&rid=giphy.gif&ct=g">'



if __name__ == "__main__":
    app.run(debug=True)