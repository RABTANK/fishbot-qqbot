import math
import random
from .constants import *
from utils import sqlite_handler as DB
from utils.time_handler import *
from .status import *


def fish(user_id, args: list,pre_message_id=None):
    back = None
    # !无参数的情况
    if not args:
        sel = DB.select(STATIC_DB_PATH, "content", "text", ["id=100001"], 1)
        if len(sel) == 1:
            back = sel[0][0]
        return back
    # !参数过多的情况
    if len(args) > 1:
        sel = DB.select(STATIC_DB_PATH, "content", "text", ["id=100003"], 1)
        if len(sel) == 1:
            back = sel[0][0]
        return back
    # !帮助
    if args[0] == "help" or args[0] == "帮助":
        sel = DB.select(STATIC_DB_PATH, "content", "text", ["id=100002"], 1)
        if len(sel) == 1:
            res = str(sel[0][0])
            sel = DB.select(STATIC_DB_PATH, "name", "fish_spot", None, 1)
            spot = ""
            for i in sel:
                spot += "\n" + i[0]
            back = res.replace("#1#", spot)
        return back
    # !地点列表
    if args[0] == "list" or args[0] == "地点":
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
        return back  
    # !正式钓鱼
    user_status = get_status(user_id)
    is_time_over: bool = (time.time() - user_status.get("status_start_time") - user_status.get("status_wait_time")) > 0
    is_status_sort_high: bool = 10 < user_status.get("status_sort")
    print(is_time_over, is_status_sort_high)
    print(user_status)
    # !状态未结束
    if not is_time_over and not is_status_sort_high:
        pass  # 占位
        status_str = status(user_id, None)
        back = DB.select(STATIC_DB_PATH, "content", "text", ["id=100005"], 1)[0][0]
        back += "\n——————————\n"
        back += status_str
        return back
    # !可以钓鱼
    else:
        input_spot = args[0]
        sel = DB.select(STATIC_DB_PATH, "*", "fish_spot", [f'name="{input_spot}"'], 2)
        # !无对应地点的状况
        if len(sel) != 1:
            back = "没有这个地点"
            return back
        # !进入对应地点
        else:
            spot = sel[0]
            set_status(
                user_id,
                100001,
                spot.get("base_time"),
                [spot.get("name"), spot.get("base_time")],
            )
            back = f"你来到了{spot.get('name')}"
            back += f"\n——————————\n"
            texts = json.loads(spot.get("texts"))
            back += f"{random.choice(texts)}"
            back += f"\n——————————\n"
            back += str(DB.select(STATIC_DB_PATH, "text", "status", ["id=100001"], 1)[0][0]).replace("#1#", spot.get("name")).replace("#2#", format_time(spot.get("base_time")))
        return back


def catch(user_id, args: list,pre_message_id=None):
    back=None
    
    return back
    
    
    
def end_fish(user_id, args: list,pre_message_id=None):
    back=None
    user_status=get_status(user_id)
    # !没有在钓鱼
    if user_status.get("status_id")!=100001:
        back=DB.select(STATIC_DB_PATH,"content","text",[f"id=100006"],1)[0][0]
        return back
    
    start_time = int(user_status.get("status_start_time"))
    wait_time = int(user_status.get("status_wait_time"))
    fish_spot = json.loads(user_status.get("status_args"))[0]
    fish_spot_id=DB.select(STATIC_DB_PATH,"id","fish_spot",[f"name='{fish_spot}'"],1)[0][0]
    fish_in_spot_ids=DB.select(STATIC_DB_PATH,"fish_id","fish_in_spot",[f"fish_spot_id={fish_spot_id}"],1)
    fish_ids= [item[0] for item in fish_in_spot_ids]
    fishs=[]
    for fish_id in fish_ids:
        fish=DB.select(STATIC_DB_PATH,"*","fish",[f"id={fish_id}"],2)[0]
        fishs.append(fish)
    back=str(fishs)
    fish_probability=1
    # !结束钓鱼，钓鱼时间未结束的状况
    if wait_time + start_time > round(time.time(), 0):
        y = 1 - math.sqrt(1 - x**2)
        pass
    # !结束钓鱼，钓鱼时间已结束的状况
    if wait_time + start_time <= round(time.time(), 0):
        pass
    return back
