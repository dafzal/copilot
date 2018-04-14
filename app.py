#Python libraries that we need to import for our bot
import random
from flask import Flask, request
app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    return "YOOO LETS GOOOO"

if __name__ == "__main__":
    app.run()