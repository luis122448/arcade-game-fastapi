from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from schemas.score_schema import ScoreSchema, ScoreSaveSchema
from services.score_service  import ScoreService
from typing import List
from config.postgres import session
# from schemas.response_schema import ResponseApi

score_router = APIRouter()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@score_router.get("/score", tags=["Game-Score"])
async def findAll(idgame: int, db: session = Depends(get_db)):
    result = jsonable_encoder(ScoreService(db).findAll(idgame))
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)

@score_router.get("/score/{id}", tags=["Game-Score"], response_model=ScoreSchema)
async def findById(idgame: int, idscore: int, db: session = Depends(get_db)):
    result = jsonable_encoder(ScoreService(db).findById(idgame, idscore))
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)

@score_router.post("/score", tags=["Game-Score"], response_model=ScoreSchema)
async def create(score: ScoreSaveSchema, db: session = Depends(get_db)):
    result = jsonable_encoder(ScoreService(db).create(score))
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)

@score_router.delete("/score/{id}", tags=["Game-Score"], response_model=ScoreSchema)
async def delete(id: int, db: session = Depends(get_db)):
    result = jsonable_encoder(ScoreService(db).delete(id))
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)