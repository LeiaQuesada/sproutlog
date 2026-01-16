from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import GardenerCreate, GardenerRead
from db_models import DBGardener

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
