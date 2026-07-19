"""
MaskaStorage — Models Package

Import all models here so that SQLAlchemy's metadata is populated
before ``Base.metadata.create_all()`` is called.
"""

from app.database.models.document import Document

__all__ = ["Document"]
