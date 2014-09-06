from main import app
from flask import render_template


@app.route('/')
def index():
    page_title = 'VPR App Template'

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
        social=social)
