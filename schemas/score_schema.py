from typing import Optional
from pydantic import BaseModel, Field

class ScoreSchema(BaseModel):

    idscore: int
    idgame: int
    ranking: int
    username: str
    score: int
    timetotal: int
    registdate: str

    model_config = {
        "orm_mode": True,
        "json_schema_extra": {
            "examples":[{
                    "idscore": 1,
                    "idgame": 1,
                    "ranking": 1,
                    "username": "Player11",
                    "score": 100,
                    "timetotal": 100,
                    "registdate": "2021-01-01 00:00:00"
                }] 
        }
    }

class ScoreSaveSchema(BaseModel):
    idscore: Optional[int] = Field(None)
    idgame: int
    ranking: Optional[int] = Field(None)
    username: str
    score: int
    timetotal: int
    registdate: str

    model_config = {
        "orm_mode": True,
        "json_schema_extra": {
            "examples":[{
                    "idgame": 1,
                    "username": "Player11",
                    "score": 100,
                    "timetotal": 100,
                    "registdate": "2021-01-01 00:00:00"
                }] 
        }
    }

class RequestScore(BaseModel):
    parameter: ScoreSchema = Field(...)