"""Module for `Database` class."""
from __future__ import annotations

from typing import Any, Dict, List, Union

from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.future.engine import Engine
from sqlalchemy.orm import Session

from autodonate.utils.config import Config

DB_DATA = Config().get("DATABASE", "sqlite:///:memory:")


class DatabaseMeta(type):
    """Database MetaClass for make Singleton pattern."""

    __instance: List[Database] = []

    def __call__(cls, *args, **kwargs) -> Database:
        """Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if len(cls.__instance) == 0:
            instance = super().__call__(*args, **kwargs)
            cls.__instance.append(instance)
        return cls.__instance[0]


class Database(metaclass=DatabaseMeta):
    """Class for database control, only here all actions with it.

    Attributes:
        engine: Engine database object.
        session: Session object, engine will create new Session every time.
        metadata: MetaData for database.
    """

    def __init__(self, engine: Engine):
        """__init__ method.

        Args:
            engine: Engine database object.
        """
        self.engine: Engine = engine
        self.session: Session = Session(self.engine)
        self.metadata: MetaData = MetaData(self.engine)

    @classmethod
    def get_instance(cls, connect_info: str = DB_DATA) -> Database:
        """Create object of `Database`.

        This method also creates tables from `db_models.py`.

        Args:
            connect_info: Connection data. (user, password etc.)

        Returns:
            Class instance.
        """
        engine: Engine = create_engine(connect_info, future=True)
        db_obj: Database = cls(engine)

        # TODO Make guide: How add tables.
        db_obj.metadata.create_all(db_obj.engine)

        return db_obj

    def execute(
        self, to_execute, params: Union[Dict[str, Any], List[Dict[str, Any]]] = {}, commit: bool = True
    ) -> CursorResult:
        """Execute command(s) to database.

        Args:
            to_execute: SQL query, sending it to sqlalchemy.
            params: Parameters which passing to query.
            commit: Save data in DB? Default: True.

        Returns:
            Raw result of database. For normal answer, use .one() or .all().
        """
        result = self.session.execute(to_execute, params)

        if commit:
            self.session.commit()
        else:
            self.session.rollback()

        return result
