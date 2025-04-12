from fastapi import FastAPI
from app.api.v1 import dicom, tasks
from app.config import settings
import uvicorn

app = FastAPI(
    title="医学影像分析系统",
    version=settings.VERSION,
    description="肿瘤影像分析后端API"
)

# 包含路由
app.include_router(dicom.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    """启动时初始化"""
    settings.setup()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )