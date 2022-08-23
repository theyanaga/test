from pydantic import BaseModel


class LinkBase(BaseModel):
    display_name: str
    url: str

class LinkCreate(LinkBase):
    pass

class Link(LinkBase):
    id: int

    class Config:
        orm_mode = True