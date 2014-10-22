import webapp2
import json


class GetAllTodos(webapp2.RequestHandler):
    def get(self):
        """Returns a JSON formatted greeting"""
        greeting = {'greeting': 'Hello there'}
        json.dumps(greeting, sort_keys=True, indent=4)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(greeting))

app = webapp2.WSGIApplication([
    webapp2.Route(r'/todos/api/v0.1.0', 
                  handler=GetAllTodos, 
                  name='get-all-todos',
                  methods=['GET']),
])
