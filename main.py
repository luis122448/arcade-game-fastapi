from fastapi import FastAPI
from middleware.error_handler import ErrorHandler
from routers.score_routers import score_router
import uvicorn
from config.postgres import base, engine
import os

app = FastAPI()
app.title = "FastAPI with SQLAlchemy"
app.version = "0.0.1"
app.description = "This is a very fancy project, with auto docs for the API and everything"
app.docs_url = "/docs"

app.add_middleware(ErrorHandler)
app.include_router(score_router)
# base.metadata.create_all(bind=engine)

@app.get("/", tags=["Home"])
async def Home():
    return {"message": "Welcome to this fantastic app!"}

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)),
                reload=True,
                )
