#!/usr/local/bin/python2.7

import sys

from main import app
from main import upload_s3
from flask_frozen import Freezer

if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
    freezer = Freezer(app)
    freezer.freeze()
    upload_s3.set_metadata()
else:
    app.run()
