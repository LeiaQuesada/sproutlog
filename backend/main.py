from fastapi import FastAPI, HTTPException
from db import (
    add_gardener,
    add_plant,
    get_gardener_by_id,
    get_plant_by_id,
    add_task,
    get_task_by_id,
    update_plant_db,
    update_task_db,
    get_all_plants,
    get_all_tasks,
)
from fastapi.middleware.cors import CORSMiddleware
from schemas import (
    GardenerCreate,
    GardenerRead,
    PlantCreate,
    PlantRead,
    PlantCareTaskCreate,
    PlantCareTaskRead,
    PlantUpdate,
    TaskUpdate,
)

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost:4173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Layer, HTTP semantics, status codes, request/response


@app.post("/gardener")
def create_gardener(name: GardenerCreate) -> GardenerRead:
    return add_gardener(name)


@app.get("/gardener/{gardener_id}")
def get_gardener(gardener_id: int) -> GardenerRead:
    gardener = get_gardener_by_id(gardener_id)
    if gardener is None:
        raise HTTPException(status_code=404, detail="No such gardener")
    return gardener


@app.post("/plant")
def create_plant(plant_deets: PlantCreate) -> PlantRead:
    return add_plant(plant_deets)


@app.get("/plant/{plant_id}")
def get_plant(plant_id: int) -> PlantRead:
    plant = get_plant_by_id(plant_id)
    if plant is None:
        raise HTTPException(status_code=404, detail="No such plant")
    return plant


@app.get("/plants")
def endpoint_get_all_plants() -> list[PlantRead]:
    return get_all_plants()


@app.patch("/plant/{plant_id}")
def update_plant(plant_id: int, updates: PlantUpdate) -> PlantRead:
    plant = update_plant_db(plant_id, updates)
    if plant is None:
        raise HTTPException(status_code=404, detail="No such plant")
    return plant


@app.post("/task")
def create_task(task: PlantCareTaskCreate) -> PlantCareTaskRead:
    return add_task(task)


@app.get("/task/{task_id}")
def get_task(task_id: int) -> PlantCareTaskRead:
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="No such task")
    return task


@app.patch("/task/{task_id}")
def update_task(task_id: int, updates: TaskUpdate) -> PlantCareTaskRead:
    task = update_task_db(task_id, updates)
    if task is None:
        raise HTTPException(status_code=404, detail="No such plant")
    return task


@app.get("/tasks")
def endpoint_get_all_tasks() -> list[PlantCareTaskRead]:
    return get_all_tasks()


# @app.post()
