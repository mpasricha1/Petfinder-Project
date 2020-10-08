from flask import Flask
app = Flask(__name__)

app.secret_key = 'secretkey'
app.config['SESSION_TYPE'] = 'filesystem'

from app import routes
