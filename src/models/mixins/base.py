from src.models.mixins.crud import CRUDMixin
from src.models.mixins.id import IdMixin
from src.models.mixins.serializer import SerializerMixin


class BaseMixin(IdMixin, SerializerMixin, CRUDMixin):
    __abstract__ = True
