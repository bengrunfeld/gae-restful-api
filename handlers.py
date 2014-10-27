import json
import webapp2

from webapp2_extras import routes


class GetAllTodos(webapp2.RequestHandler):
    def get(self):
        """GET /: Retrieve all todos"""

        greeting = {'Retrieve': "all"}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))

class GetTodo(webapp2.RequestHandler):
    def get(self, todo_id):
        """GET /<todo_id>: Retrieve a single todo"""
        
        greeting = {'Retrieve': todo_id}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))

class CreateTodo(webapp2.RequestHandler):
    def post(self):
        """POST /: Create a single todo"""

        greeting = {'Create': 'new'}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))

class UpdateTodo(webapp2.RequestHandler):
    def put(self, todo_id):
        """PUT /<todo_id>: Update a single todo"""

        greeting = {'Update': todo_id}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))

class DeleteTodo(webapp2.RequestHandler):
    def delete(self, todo_id):
        """DELETE /<todo_id>: Delete a single todo"""
        
        greeting = {'Delete': todo_id}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))

