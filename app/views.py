from index import app
from flask import render_template, request
from config import BASE_URL
from query import api_feed


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'VPR App Template'
    stories = api_feed([262757810], numResults=10)

    social = {
        'title': "",
        'subtitle': "",
        'img': "",
        'description': "",
        'twitter_text': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        stories=stories,
        page_url=page_url)
