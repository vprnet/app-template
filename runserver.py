#!/usr/local/bin/python2.7

import sys

from main import app
from upload_s3 import set_metadata
from flask_frozen import Freezer

app.debug = True

if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
    freezer = Freezer(app)
    freezer.freeze()
    set_metadata()
else:
    app.run()
