import logging
import os
from datetime import datetime

import requests

from qbot_static import Static

# 配置日志记录器
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(
                            os.path.join(Static.WORKPATH, (f"logs/err/{datetime.now().strftime('%Y%m%d')}.logs"))),
                        logging.StreamHandler()
                    ])


class GroupMessageSender:
    def __init__(self, group=None, msg_type: int = None) -> None:
        self.group = group
        self.msg_type = msg_type
        self.message = None
        self.pre_message_id = None
        self.pre_event = None
        self.markdown = None
        self.keyboard = None
        self.media = None
        self.ark = None

    async def send(self):
        sta = Static()
        url = sta.API_BASE_URL + f"/v2/groups/{self.group}/messages"
        access_token = await sta.get_access_token()
        headers = {
            "Authorization": f"QQBot {access_token}"
        }
        data = {"content": self.message, "msg_type": self.msg_type}

        if self.msg_type == 2:  # markdown
            data["markdown"] = self.markdown
        elif self.msg_type == 3:  # ark
            data["ark"] = self.ark
        elif self.msg_type == 7:  # media 富媒体
            data["media"] = self.media

        if self.pre_message_id is not None:
            data.update({"msg_id": self.pre_message_id})

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # 抛出HTTP错误
            response_data = response.json()
            print("Response:", response_data)
        except Exception as e:
            logging.error(f"Error sending message: {e}", exc_info=True)
