from flask import Flask
from threading import Thread
from web.app import run  # admin panel flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def keep_alive():
    Thread(target=run).start()
    Thread(target=lambda: app.run(host="0.0.0.0", port=8081)).start()
