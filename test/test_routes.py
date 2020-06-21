from app import app
import pytest

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

