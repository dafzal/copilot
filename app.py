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
    data = {
        'user_id': 1,
        'head_positions': [
            {
                'time_ms': 1523673929746,
                'position': [
                    [0.999838, -0.0166354, -0.00689306, 0.0],
                    [0.0176833, 0.979327, 0.201511, 0.0],
                    [0.00339834, -0.2016, 0.979462, 0.0],
                    [-0.0161541, 0.0116044, -0.358902, 1.0]
                ]
            },
            {
                'time_ms': 1523673929846,
                'position': [
                     [0.86698, -0.0411894, -0.496637, 0.0],
                     [0.0823146, 0.994725, 0.0611975, 0.0],
                     [0.491497, -0.0939376, 0.865797, 0.0],
                     [-0.0373612, 0.0185152, -0.343818, 1.0]
                ]
            },
            {
                'time_ms': 1523673929946,
                'position': [
                     [0.876514, -0.0315314, 0.480343, 0.0],
                     [0.0268818, 0.999501, 0.0165579, 0.0],
                     [-0.480626, -0.00160074, 0.876924, 0.0],
                     [-0.00508672, -0.020439, -0.439621, 1.0]
                ]
            },
            {
                'time_ms': 1523673930746,
                'position': [
                    [0.998138, -0.028353, -0.0540089, 0.0],
                    [0.0061001, 0.927367, -0.374104, 0.0],
                    [0.060693, 0.373078, 0.925813, 0.0],
                    [-0.0341526, 0.0826031, -0.546372, 1.0]
                ]
            }
        ],
        'location': {
            'lat': 37.386251,
            'lng': -122.0668649,
            'altitude_m': 50.2,
            'speed_mps': 15.64,
            'horizontal_accuracy_m': 5.2,
            'vertical_accuracy_m': 4.6
        }
    }

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

    for p in data['head_positions']:
        head_position = HeadPosition(**p)
        head_position.yaw_delta, head_position.pitch_delta, head_position.roll_delta = score(p['position'])
        point.head_positions.append(head_position)

    point.alert = alert(point.head_positions)
    point.user = user
    point.save()

    user.points.append(point)
    user.save()


    return jsonify(success=True,
                   attention=random.random(),
                   found_user=found_user,
                   pitch_delta=[hp.pitch_delta for hp in point.head_positions],
                   yaw_delta=[hp.yaw_delta for hp in point.head_positions],
                   roll_delta=[hp.roll_delta for hp in point.head_positions],
                   alert=point.alert)

def alert(head_positions):
    hit = 0
    miss = 0
    for p in head_positions:
        if p.yaw_delta + p.pitch_delta > .67:
            hit += 1
        else:
            miss += 1
    return hit > miss

# @app.route("/users", methods=['GET', 'POST'])
# def users():
#

def score(position, reference=None):
    if not reference:
        reference = [
            [1., 0., 0., 0.],
            [0., 1., 0., 0.],
            [0., 0., 1., 0.],
            [0., 0., 0., 0.]
        ]
    # [
    #     1, R, Y,
    #     R, 1, P,
    #     Y, P, 1,
    # ]
    yaw_delta = abs(reference[0][2] - position[0][2]) + abs(reference[2][0] - position[2][0])
    pitch_delta = abs(reference[1][2] - position[1][2]) + abs(reference[2][1] - position[2][1])
    roll_delta = abs(reference[0][1] - position[0][1]) + abs(reference[1][0] - position[1][0])
    return yaw_delta, pitch_delta, roll_delta
@app.route('/')
def foo():
    return 'hi'


if __name__ == "__main__":
    app.run()


