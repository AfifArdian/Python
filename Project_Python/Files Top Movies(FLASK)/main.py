import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET']
Bootstrap5(app)

# GET DATA FROM API
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

MOVIE_DB_API_KEY = os.environ['API_KEY']
TMDB_ACCESS_TOKEN = os.environ['TOKEN']
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


##CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

##CREATE FIND MOVIE FORM
class FindMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')

##CREATE RATE MOVIE FORM
class RateMovieForm(FlaskForm):
    rating = StringField(label='Your Ranting Out Of 10 e.g 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    print(all_movies)
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url=MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title}, headers={"Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"})
        response.raise_for_status()
        data = response.json()["results"]

        return render_template('select.html', option=data)
    return render_template('add.html', form=form)

@app.route("/find")
def find_movie():
    movie_id_api = request.args.get('id')
    if movie_id_api:
        response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id_api}", params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"}, headers={"Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"})
        response.raise_for_status()
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]

        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("rate_movie", id=new_movie.id))
    return redirect(url_for("home"))

@app.route("/edit", methods=['GET', 'POST'])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)

    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)