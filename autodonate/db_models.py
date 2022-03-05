"""Models for database."""
from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm.decl_api import DeclarativeMeta

from autodonate.database import Database

database: Database = Database.get_instance()
base: DeclarativeMeta = declarative_base(database.engine, database.metadata)


class FastTables:
    """Class for generate short links to tables."""

    def __init__(self, tables: List[Table]) -> None:
        """__init__ method.

        Args:
            tables: List with Table objects.
        """
        for table_num in range(len(tables)):
            exec("self.{0} = {0}".format(tables[table_num]))


# FIXME Make normal tables for production. WITH DOCSTRINGS, cofob!
class User(base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
