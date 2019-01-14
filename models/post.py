from mongoengine import Document ,StringField,ReferenceField

class Post(Document):
    title = StringField()
    content = StringField()
    owner = ReferenceField("User")  #trong "" dien vao class ma no tro toi