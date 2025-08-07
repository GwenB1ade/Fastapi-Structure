from fastapi import Request
from fastapi.responses import JSONResponse


async def exception_500(request: Request, exc):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
