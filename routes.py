"""
This file sets up a RESTful API, using HTTP methods combined with URI's to trigger
handlers that retrieve, store, update and delete resources.
"""

import webapp2

from webapp2_extras import routes

from config import config
from handlers import GetAllTodos
from handlers import GetTodo
from handlers import CreateTodo
from handlers import UpdateTodo
from handlers import DeleteTodo


app = webapp2.WSGIApplication([
    routes.PathPrefixRoute('/todos/api/v0.1.0', [
        # List all todos
        webapp2.Route('/',
                      handler=GetAllTodos,
                      name='get-all-todos',
                      methods=['GET']),
        # List one todo
        webapp2.Route('/<todo_id>',
                      handler=GetTodo,
                      name='get-all-todos',
                      methods=['GET']),
        # Create a new todo
        webapp2.Route('/',
                      handler=CreateTodo,
                      name='get-all-todos',
                      methods=['POST']),
        # Update an existing todo
        webapp2.Route('/<todo_id>',
                      handler=UpdateTodo,
                      name='get-all-todos',
                      methods=['PUT']),
        # Delete an existing todo
        webapp2.Route('/<todo_id>',
                      handler=DeleteTodo,
                      name='get-all-todos',
                      methods=['DELETE']),
    ]),
], config=config())
