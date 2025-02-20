
class CommandHandler:
    def __init__(self, raw, user_union_id,pre_message_id):
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
        return 'ok'
