from mongoengine import *                           # To define a schema for a


class User(Document):
    user_id = IntField(primary_key=True)
    incidents = ListField(ReferenceField('Incident'))
    points = ListField(ReferenceField('Point'))

    def to_json(self):
        return {
            'user_id': self.user_id
            ''
        }

class HeadPosition(EmbeddedDocument):
    time_ms = FloatField()
    position = ListField(ListField(FloatField()))
    yaw_delta = FloatField()
    pitch_delta = FloatField()
    roll_delta = FloatField()

class Location(EmbeddedDocument):
    lat = FloatField()
    lng = FloatField()
    altitude_m = FloatField()
    speed_mps = FloatField()
    horizontal_accuracy_m = FloatField()
    vertical_accuracy_m = FloatField()

class Point(Document):
    head_positions = ListField(EmbeddedDocumentField(HeadPosition))
    location = EmbeddedDocumentField(Location)
    user = ReferenceField(User)
    alert = BooleanField()

class Incident(Document):
    points = ListField(ReferenceField(Point))
