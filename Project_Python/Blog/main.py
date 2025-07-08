import requests
from flask import Flask, render_template

posts = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7").json()

app = Flask(__name__)

@app.route('/')
def gett_all_post():
    return render_template('index.html', all_posts=posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', all_posts=requested_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True, )
