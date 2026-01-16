from fastapi import FastAPI, HTTPException
from db import (
    add_gardener,
    add_plant,
    get_gardener_by_id,
    get_plant_by_id,
    add_task,
    get_task_by_id,
    update_plant_db
)
from fastapi.middleware.cors import CORSMiddleware
from schemas import (
    GardenerCreate,
    GardenerRead,
    PlantCreate,
    PlantRead,
    PlantCareTaskCreate,
    PlantCareTaskRead,
    PlantUpdate
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

@app.post("/api/gardener")
def create_gardener(name: GardenerCreate) -> GardenerRead:
    return add_gardener(name)

@app.get("/api/gardener/{gardener_id}")
def get_gardener(gardener_id: int) -> GardenerRead:
    gardener =  get_gardener_by_id(gardener_id)
    if gardener is None:
        raise HTTPException(status_code=404, detail="No such gardener")
    return gardener

@app.post("/api/plant")
def create_plant(plant_deets: PlantCreate) -> PlantRead:
    return add_plant(plant_deets)

@app.get("/api/plant/{plant_id}")
def get_plant(plant_id: int) -> PlantRead:
    plant = get_plant_by_id(plant_id)
    if plant is None:
        raise HTTPException(status_code=404, detail="No such plant")
    return plant

@app.patch("/api/plant/{plant_id}")
def update_plant(plant_id: int, updates: PlantUpdate) -> PlantRead:
    plant = update_plant_db(plant_id, updates)
    if plant is None:
        raise HTTPException(status_code=404, detail="No such plant")
    return plant

@app.post("/api/task")
def create_task(task: PlantCareTaskCreate) -> PlantCareTaskRead:
    return add_task(task)

@app.get("/api/task/{task_id}")
def get_task(task_id: int) -> PlantCareTaskRead:
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="No such task")
    return task
