import webapp2

from google.appengine.ext import ndb

class TodoModel(ndb.model):
    "Models an individual todo title"
    title = ndb.StringProperty()

