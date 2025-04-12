from fastapi import APIRouter
from app.models.schemas import StatusResponse

router = APIRouter(tags=["任务管理"])

@router.get("/status", response_model=StatusResponse)
def check_status():
    """检查服务状态"""
    return StatusResponse(
        status="running",
        message="服务运行正常"
    )