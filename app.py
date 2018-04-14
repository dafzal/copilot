#Python libraries that we need to import for our bot
import random
from flask import Flask, request, jsonify
from models import *
import json
from mongoengine import connect
import random

app = Flask(__name__)
url = 'tolipoc/63536:moc.balm.635360sd@nadnad:nad//:bdognom'[::-1]
connect(host=url)

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/ulu", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    data = request.get_json()
    print data
    # data = {
    #     'user_id': 1,
    #     'head_positions': [
    #         {
    #             'time_ms': 1523673929746,
    #             'position': [(0.749373, 0.0411, -0.660871, 0.0), (0.304131, 0.865196, 0.398668, 0.0), (0.588168, -0.499743, 0.635855, 0.0), (-0.230533, 0.252012, -0.177395, 1.0)]
    #         },
    #         {
    #             'time_ms': 1523673929846,
    #             'position': [(0.749373, 0.0411, -0.660871, 0.0), (0.304131, 0.865196, 0.398668, 0.0), (0.588168, -0.499743, 0.635855, 0.0), (-0.230533, 0.252012, -0.177395, 1.0)]
    #         },
    #         {
    #             'time_ms': 1523673929946,
    #             'position': [(0.749373, 0.0411, -0.660871, 0.0), (0.304131, 0.865196, 0.398668, 0.0), (0.588168, -0.499743, 0.635855, 0.0), (-0.230533, 0.252012, -0.177395, 1.0)]
    #         },
    #         {
    #             'time_ms': 1523673930746,
    #             'position': [(0.749373, 0.0411, -0.660871, 0.0), (0.304131, 0.865196, 0.398668, 0.0), (0.588168, -0.499743, 0.635855, 0.0), (-0.230533, 0.252012, -0.177395, 1.0)]
    #         }
    #     ],
    #     'location': {
    #         'lat': 37.386251,
    #         'lng': -122.0668649,
    #         'altitude_m': 50.2,
    #         'speed_mps': 15.64,
    #         'horizontal_accuracy_m': 5.2,
    #         'vertical_accuracy_m': 4.6
    #     }
    # }

    try:
        user = User.objects.get(user_id = data['user_id'])
        found_user = True
    except:
        print 'creating user'
        user = User(user_id=data['user_id'])
        user.save()
        found_user=False

    point = Point()
    point.location = Location(**data['location'])
    point.head_positions = [HeadPosition(**p) for p in data['head_positions']]
    point.user = user
    point.save()

    user.points.append(point)
    user.save()

    return jsonify(success=True, attention=random.random(), found_user=found_user)


@app.route('/')
def foo():
    return 'hi'


if __name__ == "__main__":
    app.run()


