from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.api.v1 import router as api_v1_router
from app.core.database import create_db
from app.core.services import security

# from sql_app import database

app = FastAPI()

app.include_router(api_v1_router)

# not yet implemented
# @app.middleware("http")
# async def check_authentication(request: Request, call_next):
#     if request.url.path.endswith("/auth"):
#         return await call_next(request)
#     if request.url.path.startswith("/room/"):
#         room_id = request.url.path.split("/")[-1]
#         if not security.is_authorized(room_id, request.cookies.get("token")):
#             response = RedirectResponse(url=f"/auth?redirect=/room/{room_id}")
#             return response
#     return await call_next(request)


create_db()

origins = [
    "https://testserver.jonngwanma.de",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.exception_handler(500)
async def server_error(request: Request, exc: Exception):
    # return templates.TemplateResponse("500.html", {"request": request, "exc": exc}, status_code=500)
    return "500 Internal Server Error" + str(exc)


if __name__ == "__main__":
    import uvicorn

    # uvicorn run for production
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                ssl_keyfile="/etc/ssl/private/privkey.pem",
                ssl_certfile="/etc/ssl/certs/fullchain.pem")
