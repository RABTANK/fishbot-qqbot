from auth.static import Static
import requests
class CommandHandler:
    def __init__(self, raw, user_union_id,pre_message_id,messgae_type,group_id):
        """初始化命令处理器实例。
        
        Args:
            raw (str): 用户发送的原始消息，以'/'开头的命令消息
            user_union_id (str): 用户的唯一标识符
            pre_message_id (int): 上一条消息的ID，用于消息链的上下文关联

        初始化流程:
            1. 去除原始消息首尾空格
            2. 拆分命令和参数
            3. 存储用户唯一ID和上条消息ID
        """
        self.messgae_type = messgae_type
        self.group_id = group_id
        self.raw = raw.strip()
        parts = self.raw.split(maxsplit=1)
        self.command = parts[0][1:]  # 去掉斜杠
        self.args = parts[1].split() if len(parts) > 1 else []
        self.user_union_id = user_union_id
        self.pre_message_id = pre_message_id

    def get_command(self):
        """返回命令"""
        return self.command

    def get_args(self):
        """返回参数列表"""
        return self.args

    def get_args_length(self):
        """返回参数列表的长度"""
        return len(self.args)

    def execute_command(self):
        commands = [self.command] + self.args
        response = requests.get(
            Static.PLUGS_URL,
            params={
                'command': commands,
                'userUnionId': self.user_union_id  # 新增用户唯一标识参数
            }
        )
        print(f"响应内容：{response.text}")
        return 'ok'