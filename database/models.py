from sqlalchemy import Column, Integer, String, VARCHAR

from .database import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    display_name = Column(VARCHAR(256), index=True)
    url = Column(VARCHAR(2083), index=True)
