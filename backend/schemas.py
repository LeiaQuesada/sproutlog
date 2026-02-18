from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Pydantic models for validation and serialization


class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GardenerCreate(ORMBase):
    name: str


class GardenerRead(ORMBase):
    id: int
    name: str


class PlantCreate(ORMBase):
    title: str
    description: str | None = None
    image_url: str | None
    is_edible: bool = False
    gardener_id: int


class PlantRead(ORMBase):
    id: int
    title: str
    description: str | None = None
    image_url: str | None
    is_edible: bool
    created_at: datetime
    gardener_id: int


class PlantUpdate(ORMBase):
    title: str | None = None
    description: str | None = None
    image_url: str | None = None
    is_edible: bool | None = None


class PlantCareTaskCreate(ORMBase):
    task_type: str
    due_at: datetime | None = None
    plant_id: int


class PlantSummary(ORMBase):
    id: int
    title: str


class PlantCareTaskRead(ORMBase):
    id: int
    task_type: str
    due_at: datetime | None
    completed_at: datetime | None
    created_at: datetime
    plant: PlantSummary


class TaskUpdate(ORMBase):
    task_type: str | None = None
    due_at: datetime | None = None
    completed_at: datetime | None = None


class PlantReadWithTasks(PlantRead):
    care_tasks: list["PlantCareTaskRead"]
