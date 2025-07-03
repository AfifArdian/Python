from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper(*args):
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "<u>"
    return wrapper

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Hello, Word!</h1>' \
           '<p>This is a Paragraph</p>' \
           '<img src="https://media2.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTdvNzJqc20zMGJ5dXZidW1wZW5udnU5cHV0anI2Z2xuNHdnZ2d1ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/UbN5sjsY2OLEgetF2e/giphy.webp" width=200>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)