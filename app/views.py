from app import app
from flask import Flask
import urllib
import json
import traceback
from flask import request, render_template


FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = '5NclPz4kdN0cX06Hy+aHzaPM8zRyoI3Xgb4NXJjtTCs='  # openssl rand -base64 32
PAGE_ACCESS_TOKEN = 'EAAKSLLFWS2gBABZBd7p8Dpndc3K533G4J33e8zBhEneiMbUvMnxBWKfzTUXRcMyZA5zf8MniYFcZCrjLWm2nVZAhZBIVsmAXZCLoH2KK6UU3jBnq0bNUGytxSPaGFBY2Qa8XFIbYno70qBizZA1qK7FB6ZBplbLlWTSEjC0Ww84W9wZDZD'


@app.route('/')
def hello_world():
    return 'Hello, World!'

def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    response.json()


def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"
