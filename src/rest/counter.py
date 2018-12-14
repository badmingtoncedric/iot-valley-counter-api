from flask import abort, request
from flask_restplus import Resource

import json

from server.instance import server
from dao.counter import *
from dao.history import *

app, api = server.app, server.api

counter = CounterDAO()
history = HistoryDAO()

def get_payload(request):
    return json.loads(request.data)

def validate_request(request):
    if not request.json:
        abort(400, 'JSON format only supported')

    payload = get_payload(request)

    if not payload.has_key('value'):
        abort(400, "You must set 'value' key")
    if not isinstance(payload["value"], int):
        abort(400, "'value' must be integer")

@api.route('/counter', endpoint='counter-get')
class Counter(Resource):
    def get(self):
        return counter.current

@api.route('/counter/add', endpoint='counter-add')
class CounterAdd(Resource):
    def post(self):
        validate_request(request)
        current = counter.get()
        value = get_payload(request)["value"]
        result = counter.add(value)
        history.add('add', value, current, result)
        return result

@api.route('/counter/substract', endpoint='counter-substract')
class CounterSubstract(Resource):
    def post(self):
        validate_request(request)
        current = counter.get()
        value = get_payload(request)["value"]
        result = counter.substract(value)
        history.add('substract', value, current, result)
        return result

@api.route('/counter/divide', endpoint='counter-divide')
class CounterDivide(Resource):
    def post(self):
        validate_request(request)
        current = counter.get()
        value = get_payload(request)["value"]
        if not value > 0:
            abort(400, "'value' must be positive (zero-division)")
        result = counter.divide(value)
        history.add('divide', value, current, result)
        return result

@api.route('/counter/multiply', endpoint='counter-multiply')
class CounterMultiply(Resource):
    def post(self):
        validate_request(request)
        current = counter.get()
        value = get_payload(request)["value"]
        result = counter.multiply(value)
        history.add('multiply', value, current, result)
        return result
