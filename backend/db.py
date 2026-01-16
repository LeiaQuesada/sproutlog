from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from schemas import GardenerCreate, GardenerRead, PlantCreate, PlantRead, PlantCareTaskCreate, PlantCareTaskRead, PlantUpdate
from db_models import DBGardener, DBPlant, DBPlantCareTask

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/sproutlog"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Data layer for persistence, queries, transactions

def add_gardener(gardener: GardenerCreate) -> GardenerRead:
    with SessionLocal() as session:
        gardener_model = DBGardener(**gardener.model_dump())
        session.add(gardener_model)
        session.commit()
        session.refresh(gardener_model)
    return GardenerRead(
        id=gardener_model.id,
        name=gardener_model.name
    )

def get_gardener_by_id(gardener_id: int) -> GardenerRead:
    with SessionLocal() as session:
        statement = select(DBGardener).where(DBGardener.id == gardener_id)
        gardener_object = session.scalar(statement)
        if gardener_object is None:
            return
    return GardenerRead(
        id=gardener_object.id,
        name=gardener_object.name
    )

def add_plant(plant_deets: PlantCreate) -> PlantRead:
    with SessionLocal() as session:
        plant_model = DBPlant(**plant_deets.model_dump())
        session.add(plant_model)
        session.commit()
        session.refresh(plant_model)
    return PlantRead(
        id=plant_model.id,
        title=plant_model.title,
        description=plant_model.description,
        image_url=plant_model.image_url,
        is_edible=plant_model.is_edible,
        created_at=plant_model.created_at,
        gardener_id=plant_model.gardener_id
    )

def get_plant_by_id(plant_id: int) -> PlantRead:
    with SessionLocal() as session:
        statement = select(DBPlant).where(DBPlant.id == plant_id)
        plant_object = session.scalar(statement)
        if plant_object is None:
            return
    return PlantRead(
        id=plant_object.id,
        title=plant_object.title,
        description=plant_object.description,
        image_url=plant_object.image_url,
        is_edible=plant_object.is_edible,
        created_at=plant_object.created_at,
        gardener_id=plant_object.gardener_id
    )

def update_plant_db(plant_id: int, updates: PlantUpdate) -> DBPlant:
    with SessionLocal() as session:
        plant = session.get(DBPlant, plant_id)
        for field, value in updates.model_dump(exclude_unset=True).items():
            setattr(plant, field, value)
        session.commit()
        session.refresh(plant)
        return plant

def add_task(task: PlantCareTaskCreate) -> PlantCareTaskRead:
    with SessionLocal() as session:
        task_model = DBPlantCareTask(**task.model_dump())
        session.add(task_model)
        session.commit()
        session.refresh(task_model)
    return PlantCareTaskRead(
        id=task_model.id,
        task_type=task_model.task_type,
        due_at=task_model.due_at,
        completed_at=task_model.completed_at,
        created_at=task_model.created_at,
        plant_id=task_model.plant_id
    )

def get_task_by_id(task_id: int) -> PlantCareTaskRead:
    with SessionLocal() as session:
        statement = select(DBPlantCareTask).where(DBPlantCareTask.id == task_id)
        task_object = session.scalar(statement)
        if task_object is None:
            return
    return PlantCareTaskRead(
        id=task_object.id,
        task_type=task_object.task_type,
        due_at=task_object.due_at,
        completed_at=task_object.completed_at,
        created_at=task_object.created_at,
        plant_id=task_object.plant_id
    )
