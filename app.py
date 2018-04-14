#Python libraries that we need to import for our bot
print 'monkey'
from gevent import monkey
import gevent
monkey.patch_all()
print 'end monkey'
import random
from flask import Flask, request, send_from_directory, jsonify
from models import *
from mongoengine import connect
import time
import uuid
import imageio

import boto

app = Flask(__name__)
url = 'tolipoc/63536:moc.balm.635360sd@nadnad:nad//:bdognom'[::-1]
connect(host=url)
conn = boto.connect_s3(anon=True)
bucket = conn.get_bucket('copilot-incident-images', validate=False)

@app.route("/", methods=['GET', 'POST'])
def index():
    return send_from_directory('static/dist', 'index.html')

@app.route('/incident', methods=['GET', 'POST'])
def create_incident():
    data = request.get_json()
    if not data:
        data = {
            'incident_id': str(uuid.uuid4()),
            'user_id': 2,
            'images': ['https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034',
                       'https://s3-us-west-1.amazonaws.com/copilot-incident-images/1_1523727678902.jpg',
                       'https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/20247743_10111537135804181_3181030631316154852_o.jpg?_nc_cat=0&oh=0d45848e8f2972545593881487840cb7&oe=5B62C3FC',
                       'https://s3-us-west-1.amazonaws.com/copilot-incident-images/1_1523727678902.jpg',
                       ],
        }


    incident_id = data.get('incident_id')
    try:
        Incident.objects.get(incident_id).delete()
    except:
        pass

    # create gif
    print 'pulling images'
    greenlets = []
    for url in data['images']:
        greenlets.append(gevent.spawn(imageio.imread, url))
    gevent.joinall(greenlets)
    print 'done pulling images'

    gif_name = '%s.gif' % incident_id
    local_name = '/tmp/%s' % gif_name
    imageio.mimsave(local_name, [x.value for x in greenlets])
    print 'done saving gif'

    key = boto.s3.key.Key(bucket)
    key.key = gif_name
    key.set_contents_from_filename(local_name)
    print 'done uploading gif'

    user_id = data.get('user_id')
    user = User.objects.get(user_id=user_id)

    issue = data.get('issue') or 'unresolved'
    incident = Incident()
    incident.incident_id = incident_id
    incident.timestamp = time.time()
    incident.incident_id = incident_id
    incident.issue = issue
    incident.user = user
    incident.images = [key.generate_url(expires_in=0, query_auth=False)]
    incident.scores = user.scores[-50:]
    incident.save()

    user.incidents.append(incident)
    user.save()
    return jsonify(incident.to_json())

@app.route('/resolve_incident', methods=['GET', 'POST'])
def resolve_incident():
    print request.data
    try:
        data = request.get_json()
    except Exception as e:
        print e
        raise
    print 'data is %s' % data
    if not data:
        incident_id = random.choice([x for x in list(Incident.objects.all()) if not x.reviewed_at] or [Incident.objects.all()[0]]).incident_id
        data = {
            'incident_id': incident_id,
            'issue': 'super happy %s' % str(uuid.uuid4())
        }
    print data
    incident_id = data['incident_id']
    issue = data['issue']

    incident = Incident.objects.get(incident_id=incident_id)
    incident.issue = issue
    incident.reviewed_at = time.time()
    incident.save()
    return jsonify(incident.to_json())

@app.route('/users')
def users():
    users = User.objects.all()
    return jsonify([u.to_json() for u in users])

@app.route('/incidents')
def incidents():
    try:
        data = request.get_json()
    except:
        data = {}

    if not data:
        data = {}
    user_id = data.get('user_id')

    all_incidents = list(Incident.objects.all())[::-1]
    unresolved = [r for r in all_incidents if not r.reviewed_at]

    if user_id:
        return jsonify([x.to_json() for x in all_incidents if x.user.user_id == user_id and ((x.issue == 'issue' and r.reviewed_at) or not r.reviewed_at)])
    else:
        return jsonify([x.to_json() for x in unresolved])

@app.route("/ulu", methods=['GET', 'POST'])
def ulu():
    data = request.get_json()
    print data
    if not data:
        data = {
            u'user_id': 2,
            u'location':
                {u'lat': 37.386251,
                 u'lng': -122.0668649,
                 u'speed_mps': 15.64,
                 u'horizontal_accuracy_m': 5.2,
                 u'vertical_accuracy_m': 4.6,
                 u'altitude_m': 50.2
                 },
            u'head_positions': [
                {u'position': [
                    [-0.9867934584617615, 0.03660966828465462, 0.1577843427658081, 0],
                    [-0.024106867611408234, 0.9300681948661804, -0.366578608751297, 0],
                    [-0.16017526388168335, -0.36554259061813354, -0.9169032573699951, 0],
                    [0.06864194571971893, 0.1950957328081131, 0.38621342182159424, 1]],
                    u'time_ms': 1523718173693},
                {u'position': [
                    [-0.9867934584617615, 0.03660966828465462, 0.1577843427658081, 0],
                    [-0.024106867611408234, 0.9300681948661804, -0.366578608751297, 0],
                    [-0.16017526388168335, -0.36554259061813354, -0.9169032573699951, 0],
                    [0.06864194571971893, 0.1950957328081131, 0.38621342182159424, 1]],
                    u'time_ms': 1523718173693}
            ],
            u'camera_positions': [
                {u'position': [
                    [0.03457019478082657, -0.8862884640693665, 0.4618278741836548, 0],
                    [-0.9986507892608643, -0.012730330228805542, 0.05032804608345032, 0],
                    [-0.03872963413596153, -0.4629458487033844, -0.8855332732200623, 0],
                    [0, 0, 0, 1]],
                    u'time_ms': 1523718173696},
                {u'position': [
                    [0.03457019478082657, -0.8862884640693665, 0.4618278741836548, 0],
                    [-0.9986507892608643, -0.012730330228805542, 0.05032804608345032, 0],
                    [-0.03872963413596153, -0.4629458487033844, -0.8855332732200623, 0],
                    [0, 0, 0, 1]],
                    u'time_ms': 1523718173696}
            ]
        }

    try:
        user = User.objects.get(user_id = data['user_id'])
    except:
        print 'creating user'
        user = User(user_id=data['user_id'])
        user.name = 'Mishall'
        user.save()

    point = Point()
    point.location = Location(**data['location'])

    for p, c in zip(data['head_positions'], data['camera_positions']):
        if p and c:
            head_position = HeadPosition(**p)
            camera_position = CameraPosition(**c)

            head_position.score = score(p['position'], c['position'])

            point.head_positions.append(head_position)
            point.camera_positions.append(camera_position)

    # point.user = user
    # point.save()

    # user.points.append(point)
    # user.save()

    user.scores.extend([hp.score for hp in point.head_positions])
    user.scores = user.scores[:500]
    user.save()

    x =  jsonify(
        success=True,
        scores = [{'score': hp.score, 'time_ms': hp.time_ms} for hp in point.head_positions]
    )
    return x

def alert(head_positions):
    hit = 0
    miss = 0
    for p in head_positions:
        if p.yaw_delta + p.pitch_delta > .67:
            hit += 1
        else:
            miss += 1
    return hit > miss

import math
def magnitude(x):
    return math.sqrt(x[0]**2 + x[1]**2 + x[2]**2)

def score2(mtrx):
    x = [x[0] for x in mtrx[:3]]
    y = [x[1] for x in mtrx[:3]]
    z = [x[2] for x in mtrx[:3]]
    print 'score2 x %s y %s z %s' % (x, y, z)

    x = magnitude(x)
    y = magnitude(y)
    z = magnitude(z)
    total = magnitude([x, y, z])
    print 'total score x %s y %s z %s total %s' % (x, y, z, total)
    return total



def score(face, camera):

    # [
    #     1, R, Y,
    #     R, 1, P,
    #     Y, P, 1,
    # ]
    transformed_face = [
        [-1*x for x in face[1]],
        [y for y in face[0]],
        [z for z in face[2]]
    ]
    delta_transform = [
        [x-y for x,y in zip(transformed_face[0], camera[0])],
        [x-y for x,y in zip(transformed_face[1], camera[1])],
        [x-y for x,y in zip(transformed_face[2], camera[2])],
    ]
    print 'face'
    for i in xrange(3):
        print ' '.join(['%.1f' % x for x in face[i][:3]])
    print 'camera'
    for i in xrange(3):
        print ' '.join(['%.1f' % x for x in camera[i][:3]])

    print 'transformed face'
    for i in xrange(3):
        print ' '.join(['%.1f' % x for x in transformed_face[i][:3]])

    print 'delta'
    for i in xrange(3):
        print ' '.join(['%.1f' % x for x in delta_transform[i][:3]])

    return score2(delta_transform)


    # yaw_delta = abs(reference[0][2] - position[0][2]) + abs(reference[2][0] - position[2][0])
    # pitch_delta = abs(reference[1][2] - position[1][2]) + abs(reference[2][1] - position[2][1])
    # roll_delta = abs(reference[0][1] - position[0][1]) + abs(reference[1][0] - position[1][0])
    # print 'Yaw %s pitch %s roll %s' % (yaw_delta, pitch_delta, roll_delta)
    # return 0, 0, 0

# def users():
#     return jsonify([
#         {
#             "img_url": "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034",
#             "name": "Dan",
#             "user_id": dan_id
#         },
#         {
#             "img_url": "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/17761164_10155154480811796_246260306778900723_o.jpg?_nc_cat=0&oh=a7d2233f1545e6ae245896de0254a3a5&oe=5B7163B4",
#             "name": "Bob",
#             "user_id": bob_id
#         }
#     ])
#
# def incidents():
#     return jsonify([
#         {
#             "incident_id": str(uuid.uuid4()),
#             "timestamp": int(time.time()),
#             "img_urls": [
#                 "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034",
#                 "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034"],
#             "issue": None,
#             "reviewed_at": None,
#             "user": {
#                 "img_url": "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034",
#                 "name": "Dan",
#                 "user_id": dan_id
#             },
#         },
#         {
#             "incident_id": str(uuid.uuid4()),
#             "timestamp": int(time.time()),
#             "img_urls": [
#                 "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034",
#                 "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034"],
#             "issue": "completely_fucked",
#             "reviewed_at": int(time.time()),
#             "user": {
#                 "img_url": "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/17761164_10155154480811796_246260306778900723_o.jpg?_nc_cat=0&oh=a7d2233f1545e6ae245896de0254a3a5&oe=5B7163B4",
#                 "name": "Bob",
#                 "user_id": bob_id
#             }
#         }
#     ])

if __name__ == "__main__":
    app.run()


