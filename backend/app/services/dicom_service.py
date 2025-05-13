import pydicom
from pathlib import Path
from pydicom.errors import InvalidDicomError
import logging
from typing import List, Dict, Optional
from app.models.schemas import DicomResult

# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 定义必需和可选标签
required_tags = {
    'PatientID': True,  # 必需且非空
    'StudyDate': False,  # 可选
    'Modality': False   # 可选
}

def validate_dicom(file_path: Path) -> bool:
    """验证DICOM文件有效性"""
    if not file_path.exists():
        logger.error(f"文件不存在: {file_path}")
        return False

    try:
        ds = pydicom.dcmread(file_path)
        logger.info(f"成功读取文件: {file_path}")

        for tag, required in required_tags.items():
            if required:
                if tag not in ds or not ds[tag].value:
                    logger.warning(f"必需的标签缺失或无效: {tag} in {file_path}")
                    return False
            else:
                if tag in ds and ds[tag].value:
                    logger.info(f"标签 {tag}: {ds[tag].value}")
                else:
                    logger.info(f"标签 {tag} 不存在或为空")

        return True
    except InvalidDicomError as e:
        logger.error(f"无效的DICOM文件: {file_path}, 错误信息: {e}")
        return False
    except Exception as e:
        logger.error(f"处理文件时发生错误: {file_path}, 错误信息: {e}")
        return False

def get_dicom_results(directory: Path) -> List[DicomResult]:
    """获取指定目录下所有DICOM文件的处理结果"""
    results = []
    for file_path in directory.glob("*.dcm"):
        try:
            ds = pydicom.dcmread(file_path)
            result = DicomResult(
                filename=file_path.name,
                patient_id=getattr(ds, 'PatientID', None),
                study_date=getattr(ds, 'StudyDate', None),
                modality=getattr(ds, 'Modality', None),
                additional_info={tag: str(value) for tag, value in ds.items() if tag not in ['PatientID', 'StudyDate', 'Modality']}
            )
            results.append(result)
        except Exception as e:
            logging.error(f"无法读取DICOM文件 {file_path}: {e}")
    return results