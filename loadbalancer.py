import random

from flask import Flask, request
import requests
import yaml


loadbalancer = Flask(__name__)
config_filepath = './config.yaml'


def load_config(path):
    with open(path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config


config = load_config(config_filepath)


@loadbalancer.route('/')
def router():
    host_header = request.headers.get('Host')
    services = config['hosts']
    for service in services:
        if host_header == service['host']:
            response = requests.get(f'http://{random.choice(service["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404


@loadbalancer.route('/<path>')
def path_router(path: str):
    services = config['paths']
    for service in services:
        if service['path'] == request.path:
            response = requests.get(f'http://{random.choice(service["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404


if __name__ == '__main__':
    loadbalancer.run(host='0.0.0.0')
