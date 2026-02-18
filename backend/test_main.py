import pytest
from fastapi.testclient import TestClient
from main import app
from db import SessionLocal
from db_models import DBGardener, DBPlant, DBPlantCareTask

client = TestClient(app)


# Fixtures for database setup/teardown
def clear_db():
    with SessionLocal() as session:
        session.query(DBPlantCareTask).delete()
        session.query(DBPlant).delete()
        session.query(DBGardener).delete()
        session.commit()


@pytest.fixture(autouse=True)
def run_around_tests():
    clear_db()
    yield
    clear_db()


def test_create_and_get_gardener():
    response = client.post("/gardener", json={"name": "Alice"})
    assert response.status_code == 200
    gardener = response.json()
    assert gardener["name"] == "Alice"
    gid = gardener["id"]
    get_response = client.get(f"/gardener/{gid}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Alice"


def test_create_and_get_plant():
    gardener = client.post("/gardener", json={"name": "Bob"}).json()
    plant_data = {
        "title": "Tomato",
        "description": "Red tomato",
        "image_url": None,
        "is_edible": True,
        "gardener_id": gardener["id"],
    }
    response = client.post("/plant", json=plant_data)
    assert response.status_code == 200
    plant = response.json()
    assert plant["title"] == "Tomato"
    get_response = client.get(f"/plant/{plant['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Tomato"


def test_update_plant():
    gardener = client.post("/gardener", json={"name": "Carl"}).json()
    plant = client.post(
        "/plant",
        json={
            "title": "Lettuce",
            "description": "Green lettuce",
            "image_url": None,
            "is_edible": False,
            "gardener_id": gardener["id"],
        },
    ).json()
    update = {"title": "Romaine", "is_edible": True}
    response = client.patch(f"/plant/{plant['id']}", json=update)
    assert response.status_code == 200
    assert response.json()["title"] == "Romaine"
    assert response.json()["is_edible"] is True


def test_create_and_get_task():
    gardener = client.post("/gardener", json={"name": "Dana"}).json()
    plant = client.post(
        "/plant",
        json={
            "title": "Rose",
            "description": "Flower",
            "image_url": None,
            "is_edible": False,
            "gardener_id": gardener["id"],
        },
    ).json()
    task_data = {"task_type": "Water", "plant_id": plant["id"]}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 200
    task = response.json()
    assert task["task_type"] == "Water"
    get_response = client.get(f"/task/{task['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["task_type"] == "Water"


def test_update_task():
    gardener = client.post("/gardener", json={"name": "Eve"}).json()
    plant = client.post(
        "/plant",
        json={
            "title": "Basil",
            "description": "Herb",
            "image_url": None,
            "is_edible": True,
            "gardener_id": gardener["id"],
        },
    ).json()
    task = client.post(
        "/tasks", json={"task_type": "Fertilize", "plant_id": plant["id"]}
    ).json()
    update = {"task_type": "Prune"}
    response = client.patch(f"/task/{task['id']}", json=update)
    assert response.status_code == 200
    assert response.json()["task_type"] == "Prune"


def test_get_all_plants_and_tasks():
    gardener = client.post("/gardener", json={"name": "Frank"}).json()
    for i in range(3):
        client.post(
            "/plant",
            json={
                "title": f"Plant{i}",
                "description": None,
                "image_url": None,
                "is_edible": False,
                "gardener_id": gardener["id"],
            },
        )
    plants = client.get("/plants").json()
    assert len(plants) == 3
    plant_id = plants[0]["id"]
    for i in range(2):
        client.post(
            "/tasks", json={"task_type": f"Task{i}", "plant_id": plant_id}
        )
    tasks = client.get("/tasks").json()
    assert len(tasks) == 2
