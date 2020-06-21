from app import app
import pytest
import json
from hypothesis import given
from hypothesis.strategies import text

@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    return app.test_client()

def test_index(client):
    response = client.get('/', follow_redirects=True)
    assert 200 == response.status_code

def test_404(client):
    response = client.get('/404', follow_redirects=True)
    assert 404 == response.status_code
    
@given(text())
def test_text_route(client, string):
    response = client.post(
        '/dummy', 
        data = {
            'string': string
            },
        follow_redirects=True)
    data = json.loads(response.get_data(as_text=True))
    print(string)
    assert string == data['dummy']