import json
import os
import time
from utils import *
import requests


class Static:
    WORKPATH = os.getcwd()
    STATIC_PATH = os.path.join(WORKPATH, "config.json")
    STATIC_DATA = json.load((open(STATIC_PATH, "r")))
    APPID = STATIC_DATA["APPID"]
    SECRET = STATIC_DATA["SECRET"]
    TOKEN = STATIC_DATA["TOKEN"]
    PLUGS_URL= STATIC_DATA["PLUGS_URL"]
    API_BASE_URL = "https://api.sgroup.qq.com"

    def __init__(self) -> None:
        pass

    async def get_access_token(self):
        file_path = os.path.join(self.WORKPATH, "auth/access_token.json")
        if not os.path.exists(file_path):
            file = open(file_path, "w")
            file.close()
        if os.path.getsize(file_path) == 0:
            await self._update_access_token()

        file = open(file_path, "r")
        access_token = json.load(file)
        file.close()
        if access_token["get_time"] + int(access_token["expires_in"]) < time.time():
            await self._update_access_token()
            file = open(file_path, "r")
            access_token = json.load(file)
            file.close()
            
        return access_token["access_token"]

    async def _update_access_token(self):
        file_path = os.path.join(self.WORKPATH, "auth/access_token.json")
        params = {
            "appId": str(self.APPID),  # 替换为实际的参数值
            "clientSecret": str(self.SECRET),  # 替换为实际的参数值
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(
                "https://bots.qq.com/app/getAppAccessToken",
                data=json.dumps(params),
                headers=headers,
            )
            response.raise_for_status()  # 检查请求是否成功
            response_data: dict = response.json()
            response_data.update({"get_time": time.time()})
            with open(file=file_path, mode="w", encoding="utf-8") as file:
                json.dump(response_data, file, ensure_ascii=False, indent=4)
                file.close()
            return response_data
        except Exception as e:
            mylogger.error(f"Error sending message: {e}", exc_info=True)
