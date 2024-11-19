import json
import re


class EventHandler:
    def __init__(self,payload):
        self.id = payload.get("id")
        self.op = payload.get("op")
        self.content = payload.get("d")
        self.message_type = payload.get("t")

class GroupAtMessageHandler(EventHandler):
    def __init__(self,payload):
        super().__init__(payload)
        self.message_raw=str(self.content.get("content")).strip()
        self.timestamp=self.content.get("timestamp")
        self.user_id=self.content.get("author").get("member_openid")
        self.user_union_id=self.content.get("author").get("union_openid")
        self.group_id=self.content.get("group_openid")
        self.message_id=self.content.get("id")
    
    def is_function_command(self)->bool:
        pattern = r'^/\w+(\s+.+)?$'
        return bool(re.match(pattern, self.message_raw))
    
    def print_main_data(self)->None:
        print(f"group:{self.group_id} user_union_id:{self.user_union_id} message:{self.message_raw}")
    
        
        
def create_message_handler(payload):
    t=payload.get("t")
    if t == "GROUP_AT_MESSAGE_CREATE":
        return GroupAtMessageHandler(payload)
    else:
        return EventHandler(payload)
    
    
    
        