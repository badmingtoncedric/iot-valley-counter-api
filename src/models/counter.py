from flask_restplus import fields
from server.instance import server

counter = server.api.model('Counter', {
    'value': fields.Integer(description='Current value of the counter')
})
