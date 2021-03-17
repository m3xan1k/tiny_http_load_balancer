import os

from flask import Flask

loadbalancer = Flask(__name__)


@loadbalancer.route('/')
def router():
    return f'{os.environ.get("APP")} app'


if __name__ == '__main__':
    loadbalancer.run(host='0.0.0.0')
