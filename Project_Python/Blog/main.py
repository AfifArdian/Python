import requests
from flask import Flask, render_template
from post import Post

posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def gett_all_post():
    return render_template('index.html', all_posts=post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    return render_template('post.html', all_posts=post_objects, id=index)

if __name__ == "__main__":
    app.run(debug=True)
