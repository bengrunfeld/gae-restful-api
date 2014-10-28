"""
Models the data that is stored in the datastore (NDB) and retrieved from it
"""

from google.appengine.ext import ndb


class TodoModel(ndb.Model):
    "Models an individual todo title"
    title = ndb.StringProperty()
