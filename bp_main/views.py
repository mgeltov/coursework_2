from flask import Blueprint, render_template, request
from utils import load_posts, get_by_pk, get_searching_post, get_by_poster, get_comment_by_post_id

bp_main = Blueprint('bp_main', __name__, template_folder='templates')

@bp_main.route('/')
def index_page():
    posts = load_posts()
    return render_template('index.html', posts = posts)

@bp_main.route('/post/<int:pk>')
def post_page(pk):
    post = get_by_pk(pk)
    comments = get_comment_by_post_id(pk)
    comments_qty = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_qty=comments_qty)

@bp_main.route('/search/', methods=["GET"])
def search_page():
    search_text = request.args.get("search_text")
    posts = get_searching_post(search_text)
    posts_qty = len(posts)
    return render_template('search.html', posts=posts, posts_qty = posts_qty, search_text=search_text)

@bp_main.route('/user/<poster_name>')
def poster_page(poster_name):
    posts = get_by_poster(poster_name)
    return render_template('user-feed.html', posts=posts, poster_name=poster_name)