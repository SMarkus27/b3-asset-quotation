from decimal import Decimal
from enum import Enum

from sqlalchemy.inspection import inspect


class SerializerMixin:
    __abstract__ = True

    def serializer(self, depth=1, skip_columns=None):
        if skip_columns is None:
            skip_columns = {"external_id", "id", "password"}


        columns = inspect(self).mapper.column_attrs
        relationships = inspect(self).mapper.relationships

        data = {}
        for column in columns:
            if column.key not in skip_columns:
                value = getattr(self, column.key)

                if isinstance(value, Enum):
                    value = value.value

                if isinstance(value, Decimal):
                    value = float(value)

                data[column.key] = value

        for relationship in relationships:
            if relationship.key not in skip_columns:
                value = getattr(self, relationship.key)

                if relationship.uselist:
                    data[relationship.key] = [item.serializer(depth - 1, skip_columns) for item in value] if depth > 0 else []
        return data

