from mongoengine import StringField, IntField, Document

class Bike(Document):
    model = StringField()
    daily_fee = IntField()
    image = StringField()
    year = IntField()