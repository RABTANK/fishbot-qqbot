from .constants import *
from utils import sqlite_handler as DB

def create_user(user_union_id:str):
    default_user = {
    "id": user_union_id,  # 假设 id 是一个空字符串，可以根据实际情况调整
    "name": "",
    "status_id": 100000,
    "status_args": None,
    "status_start_time": 0,
    "status_wait_time": 0
}
    DB.insert(USER_DATA_DB_PATH,"user",default_user)