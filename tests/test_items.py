from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models.item import Item


def test_create_item(client: TestClient) -> None:
    response = client.post(
        "/items/",
        json={"nom": "Test Item", "prix": 10.5},
    )
    data = response.json()

    assert response.status_code == 201
    assert data["nom"] == "Test Item"
    assert data["prix"] == 10.5
    assert data["id"] is not None


def test_read_items(client: TestClient, session: Session) -> None:
    item1 = Item(nom="Item 1", prix=10.0)
    item2 = Item(nom="Item 2", prix=20.0)
    session.add(item1)
    session.add(item2)
    session.commit()

    response = client.get("/items/")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["nom"] == "Item 1"
    assert data[1]["nom"] == "Item 2"


def test_read_item(client: TestClient, session: Session) -> None:
    item = Item(nom="Test Item", prix=10.0)
    session.add(item)
    session.commit()

    response = client.get(f"/items/{item.id}")
    data = response.json()

    assert response.status_code == 200
    assert data["nom"] == "Test Item"
    assert data["id"] == item.id


def test_update_item(client: TestClient, session: Session) -> None:
    item = Item(nom="Test Item", prix=10.0)
    session.add(item)
    session.commit()

    response = client.put(
        f"/items/{item.id}",
        json={"nom": "Updated Item", "prix": 15.0},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["nom"] == "Updated Item"
    assert data["prix"] == 15.0


def test_delete_item(client: TestClient, session: Session) -> None:
    item = Item(nom="Test Item", prix=10.0)
    session.add(item)
    session.commit()

    response = client.delete(f"/items/{item.id}")
    assert response.status_code == 204

    response = client.get(f"/items/{item.id}")
    assert response.status_code == 404
