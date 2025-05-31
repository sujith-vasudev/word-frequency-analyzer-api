from pydantic import BaseModel


class PublicModel(BaseModel):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
