from mongoengine import Document, StringField,IntField

class Character(Document):
    name = StringField()
    image = StringField()
    rate = IntField()

