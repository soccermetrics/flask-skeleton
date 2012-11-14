#
#   Implementation of views
#

from flask import jsonify, Response
from flask.views import MethodView

import json
from main import app

#
# error handling
#

@app.errorhandler(400)
def bad_request(error=None):
    message = {
               'status': 400,
               'message': "Bad request."
               }
    resp = jsonify(message)
    resp.status_code = 400

    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
                'status': 404,
                'message': 'Not Found: ' + request.url
              }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(500)
def internal_error(error=None):
    message = {
                'status': 500,
                'message': 'Internal error! You can try again, or send a message to the administrator.'
              }
    resp = jsonify(message)
    resp.status_code = 500
    
    return resp
    
#
# Views
#

class HelloWorldView(MethodView):

    def get(self):
    
        msg = dict(message="Hello world!")
        
        return Response(json.dumps(msg), status=200, mimetype='application/json')
        
#
# Routing
#

# hello world!
hello_view = HelloWorldView.as_view('hello_world_view')
app.add_url_rule('/', view_func=hello_view, methods=['GET',])


