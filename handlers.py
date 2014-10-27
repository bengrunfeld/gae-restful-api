import json
import webapp2


class GetAllTodos(webapp2.RequestHandler):
    def get(self):
        """GET /: Retrieve all todos"""

        message = {'Retrieve': "all"}
        json.dumps(message, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(message))


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
