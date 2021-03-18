import random

from flask import Flask, request
import requests

from constants import Backends

loadbalancer = Flask(__name__)


@loadbalancer.route('/')
def router():
    host_header = request.headers.get('Host')
    if host_header == 'www.mango.com':
        response = requests.get(f'http://{random.choice(Backends.MANGO)}')
    elif host_header == 'www.apple.com':
        response = requests.get(f'http://{random.choice(Backends.APPLE)}')
    else:
        return 'Not Found', 404
    return response.content, response.status_code


@loadbalancer.route('/mango')
def mango_path():
    response = requests.get(f'http://{random.choice(Backends.MANGO)}')
    return response.content, response.status_code


@loadbalancer.route('/apple')
def apple_path():
    response = requests.get(f'http://{random.choice(Backends.APPLE)}')
    return response.content, response.status_code


if __name__ == '__main__':
    loadbalancer.run(host='0.0.0.0')
