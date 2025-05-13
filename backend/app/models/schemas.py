from pydantic import BaseModel
from typing import Optional,List

class UploadResponse(BaseModel):
    """DICOM上传响应模型"""
    filename: str
    saved_path: str
    message: Optional[str] = None

class StatusResponse(BaseModel):
    """服务状态响应模型"""
    status: str
    message: str

class DicomResult(BaseModel):
    """DICOM文件处理结果"""
    filename: str
    patient_id: Optional[str] = None
    study_date: Optional[str] = None
    modality: Optional[str] = None
    additional_info: Optional[dict] = None  # 可选字段，用于存储额外的信息

class DicomResultsResponse(BaseModel):
    """多个DICOM文件处理结果"""
    results: List[DicomResult]