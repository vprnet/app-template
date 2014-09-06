from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL


@app.route('/')
def index():
    page_title = 'VPR App Template'
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    social = {
        'title': "",
        'subtitle': "",
        'img': "",
        'description': "",
        'twitter_text': "",
        'creator': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        social=social)
