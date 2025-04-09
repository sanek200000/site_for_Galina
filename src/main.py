from fastapi import FastAPI

from api.services import router as router_service


app = FastAPI()
app.include_router(router_service)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, host="0.0.0.0")
