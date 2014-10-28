"""
The handlers below are triggered by routes.py

They execute commands that retrieve, store, update and delete resources.
"""

import json
import webapp2

from google.appengine.ext import ndb

from models import TodoModel


class GetAllTodos(webapp2.RequestHandler):
    def get(self):
        """GET /: Retrieve all todos"""

        query_todos = TodoModel.query().fetch()
        all_todos = [p.to_dict() for p in query_todos]

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(all_todos)


class GetTodo(webapp2.RequestHandler):
    def get(self, todo_id):
        """GET /<todo_id>: Retrieve a single todo"""

        message = {'Retrieve': todo_id}
        json.dumps(message, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(message))


class CreateTodo(webapp2.RequestHandler):
    def post(self):
        """POST /: Create a single todo"""

        message = {'Create': 'new'}
        json.dumps(message, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(message))


class UpdateTodo(webapp2.RequestHandler):
    def put(self, todo_id):
        """PUT /<todo_id>: Update a single todo"""

        message = {'Update': todo_id}
        json.dumps(message, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(message))


class DeleteTodo(webapp2.RequestHandler):
    def delete(self, todo_id):
        """DELETE /<todo_id>: Delete a single todo"""

        message = {'Delete': todo_id}
        json.dumps(message, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(message))
