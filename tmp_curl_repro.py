from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
resp = client.post('/chat', json={'question': 'why europe sales are down', 'session_id': 'demo'})
print('status', resp.status_code)
print('json', resp.json())
