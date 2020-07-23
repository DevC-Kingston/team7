from app import app
from flask import Flask
import urllib
import json
import traceback
from flask import request, render_template
from credentials import credentials
from pymessenger import Bot


FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = '5NclPz4kdN0cX06Hy+aHzaPM8zRyoI3Xgb4NXJjtTCs='
PAGE_ACCESS_TOKEN = 'EAAKSLLFWS2gBABZBd7p8Dpndc3K533G4J33e8zBhEneiMbUvMnxBWKfzTUXRcMyZA5zf8MniYFcZCrjLWm2nVZAhZBIVsmAXZCLoH2KK6UU3jBnq0bNUGytxSPaGFBY2Qa8XFIbYno70qBizZA1qK7FB6ZBplbLlWTSEjC0Ww84W9wZDZD'

bot = Bot(PAGE_ACCESS_TOKEN)

"""The listen() function handles these http requests and 
checks that they contain a valid Facebook message"""
@app.route('/webhook', methods = ['GET', 'POST'])
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
                respond(sender_id, text)

        return "ok"

"""What Facebook use to verify the right server"""
def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect again"

"""Check if the message is a message from the user"""
def is_user_message(message):
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))

"""Formulate a response to the user and pass it on to a function that sends it."""
def respond(sender, message):
    response = get_bot_response(message)
    send_message(sender, response)

"""This is just a dummy function, returning a variation of what the user said. Replace this function with one connected to chatbot."""
def get_bot_response(message):
    return "This is a dummy response to '{}'".format(message)


#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

# """Handles receiving message from the  user"""
# @app.route("/", methods=['GET', 'POST'])
# def rec_message(text):
#     if request.method == 'GET':
#         """confirms all requests the bot receives came from Facebook."""
#         token_sent = request.args.get("hub.verify_token")
#         return verify_webhook(token_sent)
#     #if the request was not get, it must be POST and we can just proceed with sending a message back to user
#     else:
#         output  = request.get_json()
#         for e in output['entry']:
#             messaging = event['messaging']
#             for message in messaging:
#                 if message.get('message'):
#                     #Facebook Messenger ID for user so we know where to send response back to
#                     recipient_id = message['sender']['id']
#                     if message['message'].get('text'):
#                         response_sent_text = get_message()
#                         send_message(recipient_id, response_sent_text)
#                     #if user sends us a GIF, photo,video, or any other non-text item
#                     if message['message'].get('attachments'):
#                         response_sent_nontext = get_message()
#                         send_message(recipient_id, response_sent_nontext)
#         return "Message Processed"








# def send_message(recipient_id, text):
    #     """Send a response to Facebook"""
    #     payload = {
    #         'message': {
    #             'text': text
    #         },
    #         'recipient': {
    #             'id': recipient_id
    #         },
    #         'notification_type': 'regular'
    #     }
    #     auth = {
    #         'access_token': PAGE_ACCESS_TOKEN
    #     }
    #     response = requests.post(
    #         FB_API_URL,
    #         params=auth,
    #         json=payload
    #     )

    #     response.json()
