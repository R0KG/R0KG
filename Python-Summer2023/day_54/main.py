from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        text = function()
        return f"<b>{text}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        text = function()
        return f"<em>{text}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        text = function()
        return f"<u>{text}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_underlined
@make_emphasis
def hello_world():
    return "Hello, World!"

def hell():
    print("lol")
    
if __name__ == "__main__":
    app.run(debug=True)
