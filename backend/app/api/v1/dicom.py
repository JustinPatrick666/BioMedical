from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pathlib import Path
from app.config import settings
from app.services.dicom_service import validate_dicom
from app.models.schemas import UploadResponse

router = APIRouter(tags=["DICOM操作"])


@router.post("/upload", response_model=UploadResponse)
async def upload_dicom(file: UploadFile = File(...)):
    """
    上传DICOM医学影像文件
    - 支持.dcm格式
    - 最大50MB
    """
    try:
        # 验证文件类型
        if not file.filename.lower().endswith('.dcm'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="仅支持DICOM(.dcm)格式文件"
            )

        # 保存文件
        save_path = settings.UPLOAD_DIR / file.filename
        with open(save_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        # 验证文件有效性
        if not validate_dicom(save_path):
            save_path.unlink()  # 删除无效文件
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="无效的DICOM文件"
            )

        return UploadResponse(
            filename=file.filename,
            saved_path=str(save_path),
            message="上传成功"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"文件处理错误: {str(e)}"
        )