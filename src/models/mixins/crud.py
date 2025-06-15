from collections.abc import Sequence

from sqlalchemy import select

from src.core.config.extensions import db


class CRUDMixin:

    __abstract__ = True

    @classmethod
    def create(cls, auto_commit: bool = True, **kwargs: dict):

        try:
            instance = cls(**kwargs)
            db.session.add(instance)
            if auto_commit:
                db.session.commit()
                db.session.refresh(instance)
            return instance
        except Exception as e:
            db.session.rollback()
            raise e

    @classmethod
    def get(cls, id: int):
         return db.session.get(cls, id)

    def update(self, auto_commit: bool = True, **kwargs: dict):
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if auto_commit:
                db.session.commit()
                db.session.refresh(self)
            return self
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self, target = None, auto_commit: bool = True):

        try:
            target = target or self
            db.session.delete(target)
            if auto_commit:
                db.session.commit()
            return target
        except Exception as e:
            db.session.rollback()
            raise e

    @classmethod
    def all(cls) -> Sequence['CRUDMixin']:

        query = select(cls)
        return db.session.execute(query).scalars().all()