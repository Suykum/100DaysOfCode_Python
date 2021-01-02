import sqlalchemy
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class MovieEditForm(FlaskForm):
    ranking = IntegerField("Enter ranking data")
    rating = FloatField("Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your review", validators=[DataRequired()])
    done = SubmitField("Done")


class AddMovie(FlaskForm):
    title = StringField("Movie title", validators=[DataRequired()])
    add_movie = SubmitField("Add Movie")


# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()

new_movie = Movie(
    title="Phone Booth",
    year=2011,
    description="A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama.",
    rating=7.5,
    ranking=1,
    review="Loved it!",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"

)
new_movie2 = Movie(
    title="Drive",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://www.shortlist.com/media/images/2019/05/the-30-coolest-alternative-movie-posters-ever-2-1556670563-K61a-column-width-inline.jpg"

)


# db.session.add(new_movie)
# db.session.add(new_movie2)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.ranking).all()
    all_movies.reverse()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieEditForm()
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    if request.method == "POST":
        selected_movie.rating = form.rating.data
        selected_movie.review = form.review.data
        selected_movie.ranking = form.ranking.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=selected_movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovie()
    if request.method == "POST":
        new_movie_title = add_form.title.data
        data = select_movie(new_movie_title)
        return render_template("select.html", new_movies=data)
    return render_template("add.html", form=add_form)


def select_movie(name):
    parameters = {"apikey": "4cd1c5fb", "s": name}
    movies_endpoint = "http://www.omdbapi.com/"
    result = requests.get(movies_endpoint, params=parameters).json()
    try:
        data = result["Search"]
    except KeyError:
        data = []
    return data


@app.route("/find")
def find_movie():
    movie_id = request.args.get('imdb_id')
    parameters = {"apikey": "4cd1c5fb", "i": movie_id}
    movies_endpoint = "http://www.omdbapi.com/"
    r_movie = requests.get(movies_endpoint, params=parameters).json()
    new_film = Movie(title=r_movie["Title"], year=r_movie["Year"], description=r_movie["Plot"], rating=r_movie["imdbRating"],
                     ranking=5, review="No review yet", img_url=r_movie["Poster"])
    try:
        db.session.add(new_film)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        print("Already exist")
    return redirect(url_for('edit', id=new_film.id))


if __name__ == '__main__':
    app.run(debug=True)
