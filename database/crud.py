from sqlalchemy.orm import Session

from . import models
from . import schemas


def create_link(db: Session, link: schemas.LinkCreate):
    db_link = models.Link(display_name=link.display_name, url=link.url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link


def get_link(db: Session, link_id: int):
    return db.query(models.Link).filter(models.Link.id == link_id).first()


def get_links(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Link).offset(skip).limit(limit).all()


def get_link_by_display_name(db: Session, display_name: str):
    return db.query(models.Link).filter(models.Link.display_name == display_name).first()

