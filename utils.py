import json

def load_posts():
    json_file = "data/posts.json"
    with open(json_file, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data

def load_comments():
    json_file = "data/comments.json"
    with open(json_file, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_by_pk(pk):
    data = load_posts()
    for post in data:
        if post['pk'] == pk:
            return post

def get_searching_post(text):
    posts_res = []
    data = load_posts()
    for post in data:
        if text.lower() in post['content'].lower():
            posts_res.append(post)
    return posts_res

def get_by_poster(poster_name):
    posts_res = []
    data = load_posts()
    for post in data:
        if post['poster_name'].lower() == poster_name.lower():
            posts_res.append(post)
    return posts_res

def get_comment_by_post_id(post_id):
    comments_res = []
    data = load_comments()
    for comment in data:
        if comment['post_id'] == post_id:
            comments_res.append(comment)
    return comments_res
