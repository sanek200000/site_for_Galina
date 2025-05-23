from fastapi import FastAPI

from api.services import router as router_services
from api.auth import router as router_auth
from api.notifications import router as router_notifications


app = FastAPI()
app.include_router(router_notifications)
app.include_router(router_auth)
app.include_router(router_services)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, host="0.0.0.0")
