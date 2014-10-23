import json
import webapp2

from webapp2_extras import routes


class GetAllTodos(webapp2.RequestHandler):
    def get(self):
        """Returns a JSON formatted greeting"""

        # TODO: Should retrieve data from a datastore
        greeting = {'greeting': 'Hello there'}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))

class GetOneTodo(webapp2.RequestHandler):
    def get(self):
        """Returns a JSON formatted greeting"""

        # TODO: Should retrieve data from a datastore
        greeting = {'greeting': 'Hello there'}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))


app = webapp2.WSGIApplication([
    routes.PathPrefixRoute('/todos/api/v0.1.0', [
        webapp2.Route('<tod_id>',
                      handler=GetAllTodos,
                      name='get-all-todos',
                      methods=['GET']),
    ]),
])
