from .constants import *
from utils import sqlite_handler as DB
from utils.time_handler import *


def fish(user_id, args: list):
    back = "出错啦，请等待管理员修复"
    if not args:
        sel = DB.select(STATIC_DB_PATH, "content", "text", ["id=100001"], 1)
        if len(sel) == 1:
            back = sel[0][0]
    if len(args) > 1:
        sel = DB.select(STATIC_DB_PATH, "content", "text", ["id=100003"], 1)
        if len(sel) == 1:
            back = sel[0][0]
    if args[0] == "help" or args[0] == "帮助":
        sel = DB.select(STATIC_DB_PATH, "content", "text", ["id=100002"], 1)
        if len(sel) == 1:
            res = str(sel[0][0])
            sel = DB.select(STATIC_DB_PATH, "name", "fish_spot", None, 1)
            spot = ""
            for i in sel:
                spot += "\n" + i[0]
            print(res)
            print(spot)
            back = res.replace("#1#", spot)
    elif args[0] == "list" or args[0] == "地点":
        sel = DB.select(STATIC_DB_PATH, "*", "fish_spot", None, 2)
        res = "目前开放的渔场：\n"
        for i in sel:
            res += "——————————\n"
            i = dict(i)
            res += i.get("name") + "\n" + i.get("description") + "\n"
            res += "————\n"
            res += f"基础钓鱼时间：{format_time(i.get('base_time'))}\n"
            res += "————\n"
            res += "鱼种：\n"
            sel2 = DB.select(
                STATIC_DB_PATH,
                "name",
                "fish f join fish_in_spot fis on f.id=fis.fish_id",
                [f'fis.fish_spot_id={i.get("id")}'],
                1,
            )
            for j in sel2:
                res += j[0] + "\n"
            res += "——————————\n"
            back = res
    else:
        input_spot = args[0]
        sel = DB.select(STATIC_DB_PATH, "id", "fish_spot", [f'name="{input_spot}"'], 1)
        print(sel)
        if len(sel) == 1:
            spot_id = sel[0][0]
        else:
            back = "没有这个地点"

    return back
