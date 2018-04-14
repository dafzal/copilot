from mongoengine import *                           # To define a schema for a


class User(Document):
    user_id = IntField(primary_key=True)
    incidents = ListField(ReferenceField('Incident'))
    points = ListField(ReferenceField('Point'))

    def to_json(self):
        return {
            'user_id': self.user_id,
        }


class CameraPosition(EmbeddedDocument):
    time_ms = FloatField()
    position = ListField(ListField(FloatField()))


class HeadPosition(EmbeddedDocument):
    time_ms = FloatField()
    position = ListField(ListField(FloatField()))
    score = FloatField()

class Location(EmbeddedDocument):
    lat = FloatField()
    lng = FloatField()
    altitude_m = FloatField()
    speed_mps = FloatField()
    horizontal_accuracy_m = FloatField()
    vertical_accuracy_m = FloatField()

class Point(Document):
    head_positions = ListField(EmbeddedDocumentField(HeadPosition))
    camera_positions = ListField(EmbeddedDocumentField(CameraPosition))
    location = EmbeddedDocumentField(Location)
    user = ReferenceField(User)
    alert = BooleanField()

class Incident(Document):
    points = ListField(ReferenceField(Point))
