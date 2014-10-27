import json
import webapp2

from webapp2_extras import routes


class GetAllTodos(webapp2.RequestHandler):
    def get(self, todo_id):
        """Returns a JSON formatted greeting"""

        # TODO: Should retrieve data from a datastore
        greeting = {'greeting': todo_id}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))


app = webapp2.WSGIApplication([
    routes.PathPrefixRoute('/todos/api/v0.1.0', [
        # List all todos
        webapp2.Route('/',
                      handler=GetAllTodos,
                      name='get-all-todos',
                      methods=['GET']),
        # List one todo
        webapp2.Route('/<todo_id>',
                      handler=GetAllTodos,
                      name='get-all-todos',
                      methods=['GET']),
        # Create a new todo
        webapp2.Route('/',
                      handler=GetAllTodos,
                      name='get-all-todos',
                      methods=['POST']),
        # Update an existing todo
        webapp2.Route('/<todo_id>',
                      handler=GetAllTodos,
                      name='get-all-todos',
                      methods=['PUT']),
        # Delete an existing todo
        webapp2.Route('/<todo_id>',
                      handler=GetAllTodos,
                      name='get-all-todos',
                      methods=['DELETE']),
    ]),
])
