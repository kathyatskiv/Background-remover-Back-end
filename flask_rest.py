import json, bson
from bson.objectid import ObjectId
import datetime, time
import base64
import os, io
from random import randrange

from flask import Flask, request, send_file, make_response, jsonify, send_from_directory, url_for, redirect
from flask_cors import CORS

from u2net_test import main as mask
from compress_img import compress


app = Flask(__name__)
cors = CORS(app)

class JSONEncoder(json.JSONEncoder):
    """ extend json-encoder class"""

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

def set_json_encoder(app):
    app.json_encoder = JSONEncoder
    return None

def set_cors_headers(app):
    app.config.CORS_HEADERS = 'Content-Type'
    return None

def set_strict_slashes(app):
    app.url_map.strict_slashes = False
    return None

set_json_encoder(app)
set_cors_headers(app)
set_strict_slashes(app)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('test_data/compressed_images', filename)

@app.route('/post', methods=['Post'])
def webhook():
    file = request.files['image']; 
    filename =  str(time.time()) + '_' + file.filename
    file.save(os.path.join('uploads', filename))

    mask(filename)
    compress(filename + ".png")

    response = jsonify({
        "file": url_for('uploaded_file', filename=filename+".png")
    })
    print(response)
    return response


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'Hello, User. Server is working successfully!'


if __name__ == '__main__':
    app.run(port=5000,
    host="127.0.0.1",
    debug=True,
    use_reloader=True)




