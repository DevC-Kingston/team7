from flask import Flask

VERIFY_TOKEN = 'somerandomtokenforthis'  # openssl rand -base64 32
PAGE_ACCESS_TOKEN = 'EAAKSLLFWS2gBABZBd7p8Dpndc3K533G4J33e8zBhEneiMbUvMnxBWKfzTUXRcMyZA5zf8MniYFcZCrjLWm2nVZAhZBIVsmAXZCLoH2KK6UU3jBnq0bNUGytxSPaGFBY2Qa8XFIbYno70qBizZA1qK7FB6ZBplbLlWTSEjC0Ww84W9wZDZD'

app = Flask(__name__)
from app import views
