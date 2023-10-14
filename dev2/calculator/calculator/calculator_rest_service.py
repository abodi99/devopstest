import os
import logging
import argparse
import sys
from flask import Flask
from flask_restx import Resource, Api, fields
from calculator_helper import CalculatorHelper

import logging
flask_log = logging.getLogger('werkzeug')

app = Flask(__name__)
api = Api(app=app,
          title="Calculator API",
          description="API for Calculator.")

api.namespaces.clear()
ns = api.namespace("calculator", description="Calculator API")
api.add_namespace(ns)

calculation = api.model('Calculation', {
    'operation': fields.String(required=True, description='add, subtract, multiply, divide'),
    'operand1': fields.String(required=True, description='Operand 1'),
    'operand2': fields.String(required=True, description='Operand 2')
})

response = api.model('Response', {
    'result': fields.String(required=True, description='result')
})

class Calculation(object):
    def __init__(self):
        c = CalculatorHelper()
        self.do = {'add':c.add, 'subtract':c.subtract, 'multiply':c.multiply, 'divide':c.divide}

    def calculate(self, data):
        r = self.do[data['operation']](float(data['operand1']), float(data['operand2']))
        return {'result': r}

@ns.route('/')
class Result(Resource):
    @ns.doc('Operations: add, subtract, multiply, divide')
    @ns.expect(calculation)
    @ns.response(200, 'Calculation result', response)
    def post(self):
        return Calculation().calculate(api.payload), 200

def main(args):
    def ifenv(key, default):
        return (
            {'default': os.environ.get(key)} if os.environ.get(key)
            else {'default': default}
        )

    parser = argparse.ArgumentParser(description='Calculator server')

    parser.add_argument('--flask-port', type=int, default='5000', help='Flask port, 5000 is default')
    parser.add_argument("--loglevel", **ifenv('LOGLEVEL', 'DEBUG'), choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set Flask logging level, DEBUG is default")
    parser.add_argument('--debug', action='store_true', help='Flask debug')
    parser.add_argument('--no-debug', dest='debug', action='store_false', help='Flask no debug is default')
    parser.add_argument('-r', '--rest', action='store_true')
    parser.set_defaults(debug=True)

    args = parser.parse_args()

    # Listen on all network interfaces
    flask_log.setLevel(level = getattr(logging, args.loglevel))
    app.run('0.0.0.0', port=args.flask_port, debug=args.debug)

if __name__ == '__main__':
    main(sys.argv[1:])

