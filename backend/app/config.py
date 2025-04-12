from pathlib import Path


class Settings:
    # 应用配置
    VERSION = "1.0.0"
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8000

    # 文件存储
    UPLOAD_DIR = Path("uploads")
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

    @classmethod
    def setup(cls):
        """初始化目录结构"""
        cls.UPLOAD_DIR.mkdir(exist_ok=True)


settings = Settings()