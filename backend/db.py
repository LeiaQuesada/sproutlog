from sqlalchemy import create_engine, select
from typing import Optional
from sqlalchemy.orm import sessionmaker, joinedload
from schemas import (
    GardenerCreate,
    GardenerRead,
    PlantCreate,
    PlantRead,
    PlantCareTaskCreate,
    PlantCareTaskRead,
    PlantUpdate,
    TaskUpdate,
    PlantSummary,
)
from db_models import DBGardener, DBPlant, DBPlantCareTask


DATABASE_URL = (
    "postgresql+psycopg://postgres:postgres@localhost:5432/sproutlog"
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Data layer for persistence, queries, transactions


def add_gardener(gardener: GardenerCreate) -> GardenerRead:
    with SessionLocal() as session:
        gardener_model = DBGardener(**gardener.model_dump())
        session.add(gardener_model)
        session.commit()
        session.refresh(gardener_model)
    return GardenerRead(id=gardener_model.id, name=gardener_model.name)


def get_gardener_by_id(gardener_id: int) -> Optional[GardenerRead]:
    with SessionLocal() as session:
        statement = select(DBGardener).where(DBGardener.id == gardener_id)
        gardener_object = session.scalar(statement)
        if gardener_object is None:
            return None
    return GardenerRead(id=gardener_object.id, name=gardener_object.name)


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
        gardener_id=plant_model.gardener_id,
    )


def get_plant_by_id(plant_id: int) -> Optional[PlantRead]:
    with SessionLocal() as session:
        statement = select(DBPlant).where(DBPlant.id == plant_id)
        plant_object = session.scalar(statement)
        if plant_object is None:
            return None
    return PlantRead(
        id=plant_object.id,
        title=plant_object.title,
        description=plant_object.description,
        image_url=plant_object.image_url,
        is_edible=plant_object.is_edible,
        created_at=plant_object.created_at,
        gardener_id=plant_object.gardener_id,
    )


def get_all_plants() -> list[PlantRead]:
    with SessionLocal() as session:
        stmt = select(DBPlant)
        plant_objects = session.scalars(stmt).all()
        plants: list[PlantRead] = []
        for plant in plant_objects:
            result = PlantRead(
                id=plant.id,
                title=plant.title,
                description=plant.description,
                image_url=plant.image_url,
                is_edible=plant.is_edible,
                created_at=plant.created_at,
                gardener_id=plant.gardener_id,
            )
            plants.append(result)
        return plants


def update_plant_db(plant_id: int, updates: PlantUpdate) -> PlantRead:
    with SessionLocal() as session:
        plant = session.get(DBPlant, plant_id)
        for field, value in updates.model_dump(exclude_unset=True).items():
            setattr(plant, field, value)
        session.commit()
        session.refresh(plant)
        if plant is None:
            raise ValueError("No such plant")
        return PlantRead(
            id=plant.id,
            title=plant.title,
            description=plant.description,
            image_url=plant.image_url,
            is_edible=plant.is_edible,
            created_at=plant.created_at,
            gardener_id=plant.gardener_id,
        )


def add_task(task: PlantCareTaskCreate) -> Optional[PlantCareTaskRead]:
    with SessionLocal() as session:
        task_model = DBPlantCareTask(**task.model_dump())
        session.add(task_model)
        session.commit()
        # Query again with joinedload to ensure plant is loaded
        statement = (
            select(DBPlantCareTask)
            .options(joinedload(DBPlantCareTask.plant))
            .where(DBPlantCareTask.id == task_model.id)
        )
        task_with_plant = session.scalar(statement)
        if task_with_plant is None or task_with_plant.plant is None:
            raise ValueError(
                "Task was created but could not be retrieved with plant"
            )
        plant = task_with_plant.plant
        plant_summary = PlantSummary(id=plant.id, title=plant.title)
        return PlantCareTaskRead(
            id=task_with_plant.id,
            task_type=task_with_plant.task_type,
            due_at=task_with_plant.due_at,
            completed_at=task_with_plant.completed_at,
            created_at=task_with_plant.created_at,
            plant=plant_summary,
        )


def get_task_by_id(task_id: int) -> Optional[PlantCareTaskRead]:
    with SessionLocal() as session:
        statement = (
            select(DBPlantCareTask)
            .options(joinedload(DBPlantCareTask.plant))
            .where(DBPlantCareTask.id == task_id)
        )
        print("Statement:", statement)
        task_with_plant = session.scalar(statement)
        if task_with_plant is None or task_with_plant.plant is None:
            return None
        plant = task_with_plant.plant
        plant_summary = PlantSummary(id=plant.id, title=plant.title)
        return PlantCareTaskRead(
            id=task_with_plant.id,
            task_type=task_with_plant.task_type,
            due_at=task_with_plant.due_at,
            completed_at=task_with_plant.completed_at,
            created_at=task_with_plant.created_at,
            plant=plant_summary,
        )


def update_task_db(
    task_id: int, updates: TaskUpdate
) -> Optional[DBPlantCareTask]:
    with SessionLocal() as session:
        task = session.get(DBPlantCareTask, task_id)
        for field, value in updates.model_dump(exclude_unset=True).items():
            setattr(task, field, value)
        session.commit()
        session.refresh(task)
        return task


def get_all_tasks() -> list[PlantCareTaskRead]:
    with SessionLocal() as session:
        stmt = (
            select(DBPlantCareTask)
            .join(DBPlantCareTask.plant)
            .options(joinedload(DBPlantCareTask.plant))
        )

        task_objects = session.execute(stmt).scalars().all()
        tasks: list[PlantCareTaskRead] = []
        for task in task_objects:
            plant = task.plant
            plant_summary = PlantSummary(id=plant.id, title=plant.title)
            task_read = PlantCareTaskRead(
                id=task.id,
                task_type=task.task_type,
                due_at=task.due_at,
                completed_at=task.completed_at,
                created_at=task.created_at,
                plant=plant_summary,
            )
            tasks.append(task_read)
        return tasks


def get_task_with_plant_by_id(task_id: int) -> Optional[PlantCareTaskRead]:
    from sqlalchemy.orm import joinedload

    with SessionLocal() as session:
        statement = (
            select(DBPlantCareTask)
            .options(joinedload(DBPlantCareTask.plant))
            .where(DBPlantCareTask.id == task_id)
        )
        task_with_plant = session.scalar(statement)
        if task_with_plant is None or task_with_plant.plant is None:
            return None
        plant = task_with_plant.plant
        plant_summary = PlantSummary(id=plant.id, title=plant.title)
        return PlantCareTaskRead(
            id=task_with_plant.id,
            task_type=task_with_plant.task_type,
            due_at=task_with_plant.due_at,
            completed_at=task_with_plant.completed_at,
            created_at=task_with_plant.created_at,
            plant=plant_summary,
        )
