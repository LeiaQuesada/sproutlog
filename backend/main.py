from fastapi import FastAPI
from db import add_gardener, add_plant
from fastapi.middleware.cors import CORSMiddleware
from schemas import GardenerCreate, GardenerRead, PlantCreate, PlantRead

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost:4173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/gardener")
def create_gardener(name: GardenerCreate) -> GardenerRead:
    return add_gardener(name)

@app.post("/api/plant")
def create_plant(plant_deets: PlantCreate) -> PlantRead:
    return add_plant(plant_deets)
