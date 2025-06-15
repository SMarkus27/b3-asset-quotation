from sqlalchemy import String, Float
from sqlalchemy.orm import mapped_column, Mapped

from src.core.config.extensions import db
from src.models.mixins.base import BaseMixin


class AssetsQuotation(db.Model, BaseMixin):

    __tablename__ = "assets_quotation"

    ticker: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="asset name",
    )

    price: Mapped[Float] = mapped_column(
        Float,
        nullable=False,
        comment="asset price",
    )