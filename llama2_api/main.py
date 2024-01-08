from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

from router import api_router as project_router

app = FastAPI(
    title="LLaMa API",
)


@app.get("/health/")
def health():
    return JSONResponse({'message': 'LLaMa API server is running'})


# Adding routers
api_router = APIRouter()
api_router.include_router(project_router, prefix="")

# Adding main router
app.include_router(api_router)
