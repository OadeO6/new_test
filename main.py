from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


app = FastAPI()

@app.middleware("http")
async def header_data(request: Request, next):
    _ = await next(request)
    headers = request.headers
    if headers:
        return JSONResponse(content=dict(headers))
    return JSONResponse(content={})
