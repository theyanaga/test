from fastapi import FastAPI, HTTPException, Depends
from database import crud, models, schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/health")
def read_root():
    return "Hello World!"


@app.get("/api/links")
def get_links(skip: int = 0, limit: int = 100, db = Depends(get_db)):
    db_links = crud.get_links(db, skip, limit)
    return db_links


@app.get("/api/link/{link_id}")
def get_link(link_id: int, db = Depends(get_db)):
    db_link = crud.get_link(db, link_id)
    if db_link is None:
        raise HTTPException(status_code=400, detail="Could not find link in database")
    return db_link


@app.put("/api/link")
def create_link(link: schemas.LinkCreate, db = Depends(get_db)):
    db_link = crud.get_link_by_display_name(db, display_name=link.display_name)
    if db_link:
        raise HTTPException(status_code=400, detail="Link with that name already exists.")
    return crud.create_link(db, link)