from mongoengine import *                           # To define a schema for a


class User(Document):
    user_id = IntField(primary_key=True)
    name = StringField(default='Danial')
    incidents = ListField(ReferenceField('Incident'))
    points = ListField(ReferenceField('Point'))

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name
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
    images = ListField(StringField())
    timestamp = IntField()
    user = ReferenceField(User)
    incident_id = StringField(primary_key=True)
    issue = StringField()
    reviewed_at = IntField()
    def to_json(self):
        return {
            'incident_id': self.incident_id,
            'timestamp': self.timestamp,
            'img_urls': self.images,
            'user': self.user.to_json(),
            'issue': self.issue,
            'reviewed_at': self.reviewed_at
        }

        # {
        #     "incident_id": "dsalfjk",
        #     "timestamp": 5000,
        #     "img_urls": ["url1", "url2"],
        #     "issue": None,
        #     "reviewed_at": None,
        #     "user": {
        #         "img_url": foo.com/img2.jpg,
        #         "name": "Bob",
        #         "user_id": "100"
        #     }
        # }