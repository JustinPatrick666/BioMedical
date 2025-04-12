from pydantic import BaseModel
from typing import Optional

class UploadResponse(BaseModel):
    """DICOM上传响应模型"""
    filename: str
    saved_path: str
    message: Optional[str] = None

class StatusResponse(BaseModel):
    """服务状态响应模型"""
    status: str
    message: str