import pytest

from loadbalancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_host_routing_mango(client):
    result = client.get('/', headers={'Host': 'www.mango.com'})
    assert b'Mango app' in result.data


def test_host_routing_apple(client):
    result = client.get('/', headers={'Host': 'www.apple.com'})
    assert b'Apple app' in result.data


def test_host_routing_404(client):
    result = client.get('/', headers={'Host': 'www.asdf.com'})
    assert result.status_code == 404


def test_path_routing_mango(client):
    result = client.get('/mango')
    assert b'Mango app' in result.data


def test_path_routing_apple(client):
    result = client.get('/apple')
    assert b'Apple app' in result.data


def test_path_routing_not_found(client):
    result = client.get('/asdf')
    assert b'Not Found' in result.data
    assert result.status_code == 404
