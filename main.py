from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# from sql_app import database

app = FastAPI()

origins = [
    "https://jonngwanma.de"
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


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn

    # engine = create_engine(
    #     get_settings().db_url,
    # )
    # Base.metadata.create_all(engine)

    # uvicorn run for production
    uvicorn.run("main:app", host="0.0.0.0", port=443,
                ssl_keyfile="/etc/ssl/private/privkey.pem",
                ssl_certfile="/etc/ssl/certs/fullchain.pem")
