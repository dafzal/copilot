from mongoengine import *                           # To define a schema for a
import datetime
import time

PEOPLE = {
    'danial': 'https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/27908303_10112794674970611_8556241720083400749_o.jpg?_nc_cat=0&oh=40d3ee2a5463f952ec21683ccc80bf25&oe=5B5A4034',
    'adam': 'https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/17761164_10155154480811796_246260306778900723_o.jpg?_nc_cat=0&oh=a7d2233f1545e6ae245896de0254a3a5&oe=5B7163B4',
    'mishall': 'https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/28515964_10156038295086953_2067945832174435111_o.jpg?_nc_cat=0&oh=1f865327bcd6e72f9c9bfe771a51f579&oe=5B6B1D11'
}
class User(Document):
    user_id = IntField(primary_key=True)
    name = StringField(default='Danial')
    incidents = ListField(ReferenceField('Incident'))
    points = ListField(ReferenceField('Point'))
    user_image = StringField(default=None)

    def to_json(self):
        if self.user_image:
            image_url = self.user_image
        elif self.name.lower() in PEOPLE:
            image_url = PEOPLE[self.name.lower()]
        elif self.incidents:
            image_url = self.incidents[-1].images[0]
        else:
            image_url = ''
        return {
            'user_id': self.user_id,
            'name': self.name,
            'user_image': image_url,
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
    timestamp = IntField(default=lambda: int(time.time()))
    user = ReferenceField(User)
    incident_id = StringField(primary_key=True)
    issue = StringField()
    reviewed_at = IntField()
    def to_json(self):
        return {
            'incident_id': self.incident_id,
            'timestamp': readable_time(self.timestamp),
            'img_urls': self.images,
            'user': self.user.to_json(),
            'issue': self.issue,
            'reviewed_at': readable_time(self.reviewed_at)
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

def readable_time(ts):
    if not ts:
        return ''
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')