import re


class EventHandler:
    def __init__(self, payload):
        self.id = payload.get("id")
        self.op = payload.get("op")
        self.content = payload.get("d")
        self.message_type = payload.get("t")


class GroupAtMessageHandler(EventHandler):
    def __init__(self, payload):
        super().__init__(payload)
        self.message_raw = str(self.content.get("content")).strip()
        self.timestamp = self.content.get("timestamp")
        self.user_id = self.content.get("author").get("member_openid")
        self.user_union_id = self.content.get("author").get("union_openid")
        self.group_id = self.content.get("group_openid")
        self.message_id = self.content.get("id")

    def is_function_command(self) -> bool:
        pattern = r'^/\w+(\s+.+)?$'
        return bool(re.match(pattern, self.message_raw))

    def print_main_data(self) -> None:
        print(f"group:{self.group_id} user_union_id:{self.user_union_id} message:{self.message_raw}")

    def print_all_data(self) -> None:
        """打印事件处理器的完整数据信息
        
        输出包含：
            - 事件基础信息(id/op/type)
            - 消息原始内容
            - 时间戳
            - 用户身份信息
            - 群组信息
            - 消息ID
        """
        print(f"""
        Event ID: {self.id}
        Operation: {self.op}
        Message Type: {self.message_type}
        Raw Message: {self.message_raw}
        Timestamp: {self.timestamp}
        User ID: {self.user_id}
        Union ID: {self.user_union_id}
        Group ID: {self.group_id}
        Message ID: {self.message_id}
        """)

def create_message_handler(payload):
    t = payload.get("t")
    if t == "GROUP_AT_MESSAGE_CREATE":
        return GroupAtMessageHandler(payload)
    else:
        return EventHandler(payload)
