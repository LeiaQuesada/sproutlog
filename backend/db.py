from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from schemas import GardenerCreate, GardenerRead, PlantCreate, PlantRead
from db_models import DBGardener, DBPlant

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/sproutlog"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

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
