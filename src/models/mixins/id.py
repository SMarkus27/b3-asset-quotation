from uuid import uuid4

from sqlalchemy import Integer, func
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, MappedSQLExpression, column_property
from sqlalchemy.dialects.postgresql import BYTEA

class IdMixin:

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        unique=True,
        autoincrement=True,
        nullable=False,
        sort_order=-1,
        comment="Autoincrement Primary Key"
    )
    external_id: Mapped[bytes] = mapped_column(
        BYTEA(16),
        index=True,
        unique=True,
        nullable=False,
        default=lambda: uuid4().bytes,
        sort_order=-1,
        comment='UUID to external identification',
    )

    @declared_attr
    def external_id_str(cls) -> MappedSQLExpression[str]:
        return column_property(
            func.concat(
                func.lower(func.substring(func.encode(cls.external_id, "hex"), 1, 8)),
                '-',
                func.lower(func.substring(func.encode(cls.external_id, "hex"), 9, 4)),
                '-',
                func.lower(func.substring(func.encode(cls.external_id, "hex"), 13, 4)),
                '-',
                func.lower(func.substring(func.encode(cls.external_id, "hex"), 17, 4)),
                '-',
                func.lower(func.substring(func.encode(cls.external_id, "hex"), 21, 12)),
            ),
        )