from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

def guess_number(function):
    def wrapper(**kwargs):
        result = function(**kwargs)
        if result == random_number:
            return ('<h1 style="color: green;">You found Me</h1>'
                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
        elif result < random_number:
            return ('<h1 style="color: red;">Too low, try again!</h1>'
                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
        else:
            return ('<h1 style="color: purple;">Too high, try again!</h1>'
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')

    return wrapper

@app.route("/")
def home():
    return ('<h1>Guess a Number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route('/<int:number>')
@guess_number
def guess(number):
    return number

if __name__ == "__main__":
    app.run(debug=True)