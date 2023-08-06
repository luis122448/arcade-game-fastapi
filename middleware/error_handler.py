from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: DispatchFunction) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except HTTPException as e:
            return JSONResponse({
                "status_code": e.status_code,
                "detail": e.detail
            }, status_code=e.status_code)
        except Exception as e:
            return JSONResponse({
                "status_code": 500,
                "detail": str(e)
            }, status_code=500)