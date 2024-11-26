import json
from .constants import USER_DATA_DB_PATH, STATIC_DB_PATH
from utils import sqlite_handler as DB
from .user import create_user
import time
from utils.time_handler import *


def status(user_id: str, args: list) -> str:
    status_data = get_status(user_id)
    # print(status_data)
    back = "出错啦，请等待管理员修复"
    if status_data.get("status_id") == 100000:
        back = status_data.get("status_text")
    if status_data.get("status_id") == 100001:
        start_time = int(status_data.get("status_start_time"))
        wait_time = int(status_data.get("status_wait_time"))
        if wait_time + start_time > round(time.time(), 0):
            status_args = json.loads(status_data.get("status_args"))
            back = (
                str(status_data.get("status_text"))
                .replace("#1#", str(status_args[0]))
                .replace(
                    "#2#", format_time(int(start_time + wait_time - round(time.time(), 0)))
                )
            )
        else:
            res=DB.select(STATIC_DB_PATH, "content", "text", [f'id={100004}'], 1)
            back = res[0][0]
    return back


def get_status(user_id: str) -> dict:
    res1 = DB.select(USER_DATA_DB_PATH, "*", "user", [f'id="{user_id}"'], 2)
    if not res1:
        create_user(user_id)
        res1 = DB.select(USER_DATA_DB_PATH, "*", "user", [f'id="{user_id}"'], 2)
    res1 = res1[0]
    res2 = DB.select(
        STATIC_DB_PATH,
        "sort as status_sort,text as status_text,name_cn as status_name,args_need",
        "status",
        [f'id={res1.get("status_id")}'],
        2,
    )
    res2 = res2[0]
    res1.update(res2)
    return res1


def set_status(
    user_id: str, status_id: int, wait_time: int = None, args: list = None
) -> str:
    res1 = DB.select(USER_DATA_DB_PATH, "*", "user", [f'id="{user_id}"'], 2)
    if not res1:
        create_user(user_id)
    DB.update(USER_DATA_DB_PATH, "user", {"status_id": status_id}, [f'id="{user_id}"'])
    DB.update(
        USER_DATA_DB_PATH,
        "user",
        {"status_start_time": round(time.time(), 0)},
        [f'id="{user_id}"'],
    )
    if wait_time:
        DB.update(
            USER_DATA_DB_PATH,
            "user",
            {"status_wait_time": wait_time},
            [f'id="{user_id}"'],
        )
    if args:
        DB.update(
            USER_DATA_DB_PATH,
            "user",
            {"status_args": json.dumps(args)},
            [f'id="{user_id}"'],
        )


def test(user_id: str, args: list = [100001]) -> str:
    set_status(user_id, args[0])
    return "test"
