import random
import requests
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    response_gender = requests.get(url=gender_url)
    response_gender.raise_for_status()
    data_gender = response_gender.json()

    response_age = requests.get(url=age_url)
    response_age.raise_for_status()
    data_age = response_age.json()

    return render_template('guess.html', person_name=name, gender=data_gender['gender'], age=data_age['age'])

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_post = response.json()

    return render_template('blog.html', posts=all_post)




if __name__ == "__main__":
    app.run(debug=True)