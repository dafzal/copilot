#Python libraries that we need to import for our bot
import random
from flask import Flask, request
import json

app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/ulu", methods=['GET', 'POST'])
def receive_message():
    print request.get_json()
    return "YOOO LETS GOOOO2"

if __name__ == "__main__":
    app.run()