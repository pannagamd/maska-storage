"""
MaskaStorage — SQLAlchemy Declarative Base
============================================
All ORM model classes inherit from ``Base``.
No CRUD or business logic here.
"""

from sqlalchemy.orm import DeclarativeBase, MappedColumn, declared_attr


class Base(DeclarativeBase):
    """
    Common base class for all SQLAlchemy ORM models.

    Provides:
    - Automatic ``__tablename__`` derived from the class name (snake_case).
    - A future hook for common columns (e.g., ``created_at``, ``updated_at``).
    """

    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        """Derive table name from class name: ``MyModel`` → ``my_model``."""
        import re

        name = cls.__name__
        # Insert underscore before uppercase letters and lowercase the result
        s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
