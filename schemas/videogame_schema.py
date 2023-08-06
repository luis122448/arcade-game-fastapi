from typing import Optional
from pydantic import BaseModel, Field

class VideogameSchema(BaseModel):

    idgame: Optional[int] = Field(None)
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    timelimit: Optional[int] = Field(None)
    maxscore: Optional[int] = Field(None)
    minscore: Optional[int] = Field(None)
    maxranking: Optional[int] = Field(None)