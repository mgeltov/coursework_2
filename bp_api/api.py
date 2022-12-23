from flask import jsonify, Blueprint
from logger import get_logger
from utils import load_posts, get_by_pk

bp_api = Blueprint('bp_api', __name__)

logger = get_logger(__name__)

@bp_api.route('/api/posts')
def posts_api():
    logger.info("accessing an api")
    posts = load_posts()
    return jsonify(posts)

@bp_api.route('/api/post/<int:pk>')
def post_api(pk):
    logger.info("accessing an api/")
    post = get_by_pk(pk)
    return jsonify(post)
