from flask import Flask
from flask_restplus import Api, Resource, fields

from server.instance import server
from dao.history import *

app, api = server.app, server.api

history = HistoryDAO()

@api.route('/history', endpoint='history')
class History(Resource):
    def get(self):
        return history.list()
    def delete(self):
        return history.reset()
