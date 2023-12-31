from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, эта модель дописывает текст в стиле Лавкрафта. Она работает с API."}

def test_answer_endpoint():
    text = {"text": "В начале своего пути"}
    response = client.post("/answer/", json=text)
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert len(response.json()) > 0