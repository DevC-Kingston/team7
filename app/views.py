from app import app
from flask import Flask
import urllib
import json
import traceback
from flask import request


# VERIFY_TOKEN = 'your verify token'  # openssl rand -base64 32
# PAGE_ACCESS_TOKEN = 'EAAKSLLFWS2gBABZBd7p8Dpndc3K533G4J33e8zBhEneiMbUvMnxBWKfzTUXRcMyZA5zf8MniYFcZCrjLWm2nVZAhZBIVsmAXZCLoH2KK6UU3jBnq0bNUGytxSPaGFBY2Qa8XFIbYno70qBizZA1qK7FB6ZBplbLlWTSEjC0Ww84W9wZDZD'

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/webhook', methods=['GET'])
def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        print("verified")
        return req.args.get("hub.challenge")
    else:
        return "incorrect"


