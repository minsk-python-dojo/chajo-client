import pytest
from client import BaseClient


@pytest.fixture
def client():
    return BaseClient('http://127.0.0.1') 


def test_check_ping_response_returns_true_when_json_contains_status_ok(client):
    ping_response = {'status': 'OK'}
    check_result: bool = client.check_ping_response(ping_response) 
    assert check_result


def test_check_ping_response_returns_false_when_json_contains_status_not_ok(client):
    ping_response = {'status': 'Not OK'}
    check_result: bool = client.check_ping_response(ping_response)
    assert not check_result


def test_check_ping_response_returns_false_when_json_does_not_contains_status(client):
    ping_response = {}
    check_result: bool = client.check_ping_response(ping_response)
    assert not check_result

def test_check_ping_response_returns_false_when_input_is_not_json(client):
    invalid_ping_response = 'OK'
    check_result: bool = client.check_ping_response(invalid_ping_response)
    assert not check_result


