def format_time(seconds: int) -> str:
    """
    将秒数转换为 "H:Min:Sec" 或 "Min:Sec" 格式的字符串。

    Args:
        seconds (int): 输入的秒数。

    Returns:
        str: 转换后的 "H:Min:Sec" 或 "Min:Sec" 格式的字符串。
    """
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    remaining_seconds = remaining_seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{remaining_seconds:02d}"
    else:
        return f"{minutes}:{remaining_seconds:02d}"