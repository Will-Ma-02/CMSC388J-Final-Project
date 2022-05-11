from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

from .. import movie_client
from ..forms import NewThreadForm, NewPostForm
from ..models import User, Review, Thread, Post
from ..utils import current_time

movies = Blueprint("movies", __name__)

@movies.route("/", methods=["GET", "POST"])
def index(): 
    return render_template("index.html")

"""
@movies.route("/search-results/<query>", methods=["GET"])
def query_results(query):
    try:
        results = movie_client.search(query)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("movies.index"))

    return render_template("query.html", results=results)


@movies.route("/movies/<movie_id>", methods=["GET", "POST"])
def movie_detail(movie_id):
    try:
        result = movie_client.retrieve_movie_by_id(movie_id)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("movies.login"))

    form = MovieReviewForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        review = Review(
            commenter=current_user._get_current_object(),
            content=form.text.data,
            date=current_time(),
            imdb_id=movie_id,
            movie_title=result.title,
        )
        review.save()

        return redirect(request.path)

    reviews = Review.objects(imdb_id=movie_id)

    return render_template(
        "movie_detail.html", form=form, movie=result, reviews=reviews
    )
"""

@movies.route("/user/<username>")
def user_detail(username):
    user = User.objects(username=username).first()
    reviews = Review.objects(commenter=user)

    return render_template("user_detail.html", username=username, reviews=reviews)


@movies.route("/action", methods=["GET", "POST"])
def action_board():

    form = NewThreadForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        thread = Thread(
            original=current_user._get_current_object(),
            topic= form.subject.data,
            description=form.content.data,
            thread_image=form.picture.data,
            genre="action"
        )

        thread.save()
        return redirect(request.path)

    threads = Thread.objects(genre="action")
    
    return render_template(
        "action.html", form=form, threads=threads
    )

@movies.route("/action/<topic>", methods=["GET", "POST"])
def action_thread(topic):
    form = NewPostForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        post = Post(
            commenter=current_user._get_current_object(),
            content=form.text.data,
            date=current_time(),
            topic=topic
        )

        post.save()
        return redirect(request.path)

    posts = Post.objects(topic=topic)
    
    return render_template(
        "action_thread.html", form=form, posts=posts, 
    )

@movies.route("/horror", methods=["GET", "POST"])
def horror_board():

    form = NewThreadForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        thread = Thread(
            original=current_user._get_current_object(),
            topic= form.subject.data,
            description=form.content.data,
            thread_image=form.picture.data,
            genre="horror"
        )

        thread.save()
        return redirect(request.path)

    threads = Thread.objects(genre="horror")
    
    return render_template(
        "horror.html", form=form, threads=threads
    )

@movies.route("/mystery", methods=["GET", "POST"])
def mystery_board():

    form = NewThreadForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        thread = Thread(
            original=current_user._get_current_object(),
            topic= form.subject.data,
            description=form.content.data,
            thread_image=form.picture.data,
            genre="mystery"
        )

        thread.save()
        return redirect(request.path)

    threads = Thread.objects(genre="mystery")
    
    return render_template(
        "mystery.html", form=form, threads=threads
    )

@movies.route("/romance", methods=["GET", "POST"])
def romance_board():

    form = NewThreadForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        thread = Thread(
            original=current_user._get_current_object(),
            topic= form.subject.data,
            description=form.content.data,
            thread_image=form.picture.data,
            genre="romance"
        )

        thread.save()
        return redirect(request.path)

    threads = Thread.objects(genre="romance")
    
    return render_template(
        "romance.html", form=form, threads=threads
    )

@movies.route("/documentary", methods=["GET", "POST"])
def documentary_board():

    form = NewThreadForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        thread = Thread(
            original=current_user._get_current_object(),
            topic= form.subject.data,
            description=form.content.data,
            thread_image=form.picture.data,
            genre="documentary"
        )

        thread.save()
        return redirect(request.path)

    threads = Thread.objects(genre="documentary")
    
    return render_template(
        "documentary.html", form=form, threads=threads
    )




