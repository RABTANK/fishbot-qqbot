import logging
from datetime import datetime
import os

# 配置日志记录器
log_directory = os.path.join(os.getcwd(),"logs") # 替换为你的日志目录
log_filename = f"{datetime.now().strftime('%Y%m%d')}.log"
log_file_path = f"{log_directory}/{log_filename}"

class LoggerSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if LoggerSingleton._instance is None:
            LoggerSingleton._instance = LoggerSingleton()
        return LoggerSingleton._instance

    def __init__(self):
        if LoggerSingleton._instance is not None:
            raise Exception("This is a singleton class")
        self.setup_logger()

    def setup_logger(self):
        logging.basicConfig(
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file_path),
                logging.StreamHandler()
            ]
        )

def get_logger(name):
    LoggerSingleton.get_instance()
    return logging.getLogger(name)

mylogger=get_logger(None)