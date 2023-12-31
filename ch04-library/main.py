import uvicorn
from fastapi import FastAPI, Depends
from controllers import admin, management
from configuration.config import LibrarySettings

app = FastAPI()
app.include_router(admin.router, prefix="/ch04/library")
app.include_router(management.router, prefix="/ch04/library")


def build_config():
    return LibrarySettings()


@app.get("/index")
def index_library(config: LibrarySettings = Depends(build_config)):
    return {
        "project_name": config.application,
        "webmaster": config.webmaster,
        "created": config.created,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
