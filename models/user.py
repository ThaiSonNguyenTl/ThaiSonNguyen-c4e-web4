from mongoengine import Document, StringField


class User(Document):
    username = StringField() #ko dc luu password that vao 
    password = StringField()



