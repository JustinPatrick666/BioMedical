import pydicom
from pathlib import Path
from pydicom.errors import InvalidDicomError

def validate_dicom(file_path: Path) -> bool:
    """验证DICOM文件有效性"""
    try:
        ds = pydicom.dcmread(file_path, force=True)
        required_tags = ['PatientID', 'StudyDate', 'Modality']
        return all(tag in ds for tag in required_tags)
    except InvalidDicomError:
        return False