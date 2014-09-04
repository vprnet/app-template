#!/usr/local/bin/python2.7

import os
import hashlib
import gzip
import time
import datetime
import mimetypes

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from config import (AWS_KEY, AWS_SECRET_KEY, AWS_BUCKET, AWS_DIRECTORY,
    HTML_EXPIRES, STATIC_EXPIRES, ABSOLUTE_PATH)

PUSH_FROM = ABSOLUTE_PATH + 'build'


def get_files(directory):
    """Gets full path of all files within directory, including subdirectories
    Returns a list of paths"""

    file_paths = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            filepath = os.path.join(root, f)
            file_paths.append(filepath)

    return file_paths


def expires_header(duration):
    """Takes a number of seconds and turns it into an expires header"""

    return time.strftime("%a, %d-%b-%Y %T GMT",
        time.gmtime(time.time() + duration))


def gzip_file(filename):
    """Does what you think it does"""

    f_in = open(filename, 'rb')
    with gzip.open(filename + '.gz', 'w+') as f:
        f.writelines(f_in)
    f_in.close()
    f = filename + '.gz'
    return f


def set_metadata():
    """Take a list of files to be uploaded to s3 and gzip CSS, JS, and HTML,
    setting metadata for all files"""

    gzip_extensions = ['.html', '.js', '.css']

    upload_list = get_files(PUSH_FROM)
    conn = S3Connection(AWS_KEY, AWS_SECRET_KEY)
    mybucket = conn.get_bucket(AWS_BUCKET)

    static_expires = expires_header(STATIC_EXPIRES)
    html_expires = expires_header(HTML_EXPIRES)

    # define all necessary attributes of each file for s3
    for filename in upload_list:
        k = Key(mybucket)
        ext = os.path.splitext(filename)[1]
        web_path = filename.split('build/')[1]

        # Set expires for HTML, remove extension if not index
        if ext == '.html':
            if 'index' not in web_path:
                k.key = AWS_DIRECTORY + os.path.splitext(web_path)[0]
            else:
                k.key = AWS_DIRECTORY + web_path
            k.set_metadata('Expires', html_expires)
        else:
            k.key = AWS_DIRECTORY + web_path  # strip leading 0
            k.set_metadata('Expires', static_expires)

        if ext in gzip_extensions:
            f = gzip_file(filename)
            k.set_metadata('Content-Encoding', 'gzip')
        else:
            f = filename

        k.set_metadata('Content-Type', mimetypes.types_map[ext])
        etag_hash = hashlib.sha1(f + str(time.time())).hexdigest()
        k.set_metadata('ETag', etag_hash)
        k.set_contents_from_filename(f)
        k.make_public()

    print '\nPage successfully updated'
    print "On " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
