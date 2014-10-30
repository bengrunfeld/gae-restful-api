"""
The handlers below are triggered by routes.py

They execute commands that retrieve, store, update and delete resources.
"""

import json
import webapp2
import datetime

from google.appengine.ext import ndb

from models import TodoModel


def build_new_dict(data):
    """Build a new dict so that the data can be JSON serializable"""

    result = data.to_dict()
    record = {}

    # Populate the new dict with JSON serializiable values
    for key in result.iterkeys():
        if isinstance(result[key], datetime.datetime):
            record[key] = result[key].isoformat()
            continue
        record[key] = result[key]
    
    # Add the key so that we have a reference to the record
    record['key'] = data.key.id()

    return record
        

def serialize_data(qry):
    """serialize ndb return data so that we can convert it to JSON"""
    
    # check if qry is a list (multiple records) or not (single record)
    data = []
    
    if type(qry) != list: 
        record = build_new_dict(qry) 
        return record

    for q in qry:
        data.append(build_new_dict(q))

    return data 


class GetAllTodos(webapp2.RequestHandler):
    def get(self):
        """GET /: Retrieve all todos"""

        try:
            qry = TodoModel.query().fetch()
            all_todos = serialize_data(qry)

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write(json.dumps(all_todos, sort_keys=True, indent=4))
        except:
            # TODO: Improve this error 
            raise Exception("Error: could not complete request")            


class GetTodo(webapp2.RequestHandler):
    def get(self, todo_id):
        """GET /<todo_id>: Retrieve a single todo"""

        try:
            qry = ndb.Key('TodoModel', int(todo_id))
            record = serialize_data(qry.get())
            
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write(json.dumps(record, sort_keys=True, indent=4))
        except:
            raise Exception("Error: could not complete request")


class CreateTodo(webapp2.RequestHandler):
    def post(self):
        """POST /: Create a single todo"""

        try:
            new_todo = TodoModel(title = self.request.get('title')) 
            key = new_todo.put()

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Successfully added new todo')
        except:
            raise Exception("Error: could not complete request")


class UpdateTodo(webapp2.RequestHandler):
    def put(self, todo_id):
        """PUT /<todo_id>: Update a single todo""" 
        
        try:
            qry = ndb.Key('TodoModel', int(todo_id))
            target = qry.get()
            target.title = self.request.get('title')
            target.put()
            
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Record was updated')
        except:
            raise Exception("Error: could not complete request")


class DeleteTodo(webapp2.RequestHandler):
    def delete(self, todo_id):
        """DELETE /<todo_id>: Delete a single todo"""

        try:
            qry = ndb.Key('TodoModel', int(todo_id))
            qry.delete()

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('{} was deleted'.format(todo_id))
        except:
            raise Exception("Error: could not complete request")
