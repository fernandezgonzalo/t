import os
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
from peewee import IntegerField

DATABASE_NAME = 'task.db'
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)
db = SqliteDatabase(DATABASE_PATH)


class Base(Model):
    class Meta:
        database = db


class Task(Base):
    desc = CharField()
    priority = IntegerField(default=0)

    class Meta:
        order_by = ('-priority',)


db.connect()
db.create_tables([Task], safe=True)
