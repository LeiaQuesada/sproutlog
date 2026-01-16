from datetime import datetime
from sqlalchemy import Text, Boolean, DateTime, ForeignKey, func

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)


class Base(DeclarativeBase):
    pass


class DBGardener(Base):
    __tablename__ = "gardeners"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    plants: Mapped[list["DBPlant"]] = relationship(back_populates="gardeners", cascade="all, delete-orphan")


class DBPlantCareTask(Base):
    __tablename__ = "plant_care_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_type: Mapped[str] = mapped_column(Text, nullable=False)
    due_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    # Note the type hint here has to be quoted
    # because DBPlant isn't defined yet
    # This creates a property on DBPlantCareTask objects called .plant
    # Which contains a DBPlant object
    # This creates a foreign key of plant_id
    plant_id: Mapped[int] = mapped_column(
        ForeignKey("plants.id", ondelete="CASCADE"),
        nullable=False
    )
    plant: Mapped["DBPlant"] = relationship(back_populates="plant_care_task")

class DBPlant(Base):
    __tablename__ = "plants"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    image_url: Mapped[str | None] = mapped_column(Text)
    is_edible: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="false"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    # This creates a magic property on any author object
    # that when accessed gives you a list of books.
    # Under the hood this would perform a join
    care_tasks: Mapped[list[DBPlantCareTask]] = relationship(
        back_populates="plants", cascade="all, delete-orphan"
    )
