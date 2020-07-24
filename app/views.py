
from app import app
from flask import Flask, request
import urllib
import json
import traceback
import requests
from credentials import credentials
from pymessenger import Bot


FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = '5NclPz4kdN0cX06Hy+aHzaPM8zRyoI3Xgb4NXJjtTCs='  # openssl rand -base64 32
PAGE_ACCESS_TOKEN = 'EAAKSLLFWS2gBABZBd7p8Dpndc3K533G4J33e8zBhEneiMbUvMnxBWKfzTUXRcMyZA5zf8MniYFcZCrjLWm2nVZAhZBIVsmAXZCLoH2KK6UU3jBnq0bNUGytxSPaGFBY2Qa8XFIbYno70qBizZA1qK7FB6ZBplbLlWTSEjC0Ww84W9wZDZD'


"""What Facebook use to verify the right server"""
def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect again"


"""The listen() function handles these http requests and 
checks that they contain a valid Facebook message"""
@app.route('/webhook', methods=['GET', 'POST'])
def listen():
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
               text = x['message']['text']
               sender_id = x['sender']['id']
               return respond(sender_id, response)
              #respond(sender_id, text)
        return "ok"


"""Check if the message is a message from the user"""
def is_user_message(message):
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


"""Formulate a response to the user and pass it on to a function that sends it."""
def respond(sender, message):
    response = get_bot_response(message)
    send_message(sender, message)
    return "ok"


#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

