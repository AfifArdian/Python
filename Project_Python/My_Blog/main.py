import requests
import os
import smtplib
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

MY_EMAIL = os.environ['EMAIL']
MY_PASSWORD = os.environ['PASSWORD']

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data["username"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]

        print(name)
        print(email)
        print(phone)
        print(message)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:NEW MESSAGE!\n\nNama: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
