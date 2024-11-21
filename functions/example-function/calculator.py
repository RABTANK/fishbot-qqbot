import random


def add(expression: list) -> str:
    if not expression:
        return "没有参数"
    non_digit_indices = [i + 1 for i, arg in enumerate(expression) if not arg.isdigit()]
    if non_digit_indices:
        return f"第{', '.join(map(str, non_digit_indices))}个参数不是数字"
    total = sum(int(arg) for arg in expression)
    return str(total)

