from flask import Flask

loadbalancer = Flask(__name__)


@loadbalancer.route('/')
def router():
    return 'hello'


if __name__ == '__main__':
    loadbalancer.run(host='0.0.0.0')
