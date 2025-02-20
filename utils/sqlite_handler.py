from .logger import get_logger
import sqlite3

mylogger=get_logger("sqliteHandler")
def select(database: str, target: str = "*", table: str = None, condition: list = None, res_type: int = 0):
    """
    查询数据库并返回指定格式的结果。
    Args:
        database (str): 数据库文件的路径。
        target (str): 查询的目标字段或表达式。
        table (str): 要查询的表名。
        condition (list): 查询条件列表，每个条件是一个字符串。
        res_type (int): 结果的返回类型。
            0: 元组列表
            1: 二重列表
            2: 字典列表，键为列名，值为值
    Returns:
        list: 查询结果，根据 `res_type` 参数的不同，返回元组列表、二重列表或字典列表。
    """
    sql = "SELECT {} FROM {}".format(target, table)
    if condition:
        sql += " WHERE {}".format(" AND ".join(condition))
    
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        # 获取列名
        column_names = [description[0] for description in cur.description]
        conn.commit()
        conn.close()
        
        
        if res_type == 0:
            return res
        elif res_type == 1:
            return [list(tup) for tup in res]
        elif res_type == 2:
            return [dict(zip(column_names, row)) for row in res]
        else:
            raise ValueError("Invalid res_type. Valid values are 0, 1, or 2.")
    except sqlite3.Error as e:
        print("sql查询错误：{}".format(sql))
        return None


def insert(database: str, table: str, data: dict) -> bool:
    """
    向数据库中插入数据。
    Args:
        database (str): 数据库文件的路径。
        table (str): 要插入数据的表名。
        values (dict): 要插入的数据，以字典形式表示，键为列名，值为对应的值。
    Returns:
        bool: 插入操作是否成功。
    """
    try:
        # 连接到数据库
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        # 构建插入语句
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        values = tuple(data.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        print("sql查询：{}".format(query))
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    except Exception as e:
        mylogger.error(e)
        return False


def update(database: str, table: str, data: dict, condition: list = None) -> bool:
    """
    更新数据库中的数据。
    Args:
        database (str): 数据库文件的路径。
        table (str): 要更新数据的表名。
        data (dict): 要更新的数据，以字典形式表示，键为列名，值为对应的值。
        condition (list): 更新条件列表，每个条件是一个字符串。
    Returns:
        bool: 更新操作是否成功。
    """
    try:
        # 连接到数据库
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        # 构建更新语句
        set_clause = ", ".join([f"{column} =?" for column in data.keys()])
        values = tuple(data.values())
        query = f"UPDATE {table} SET {set_clause}"
        if condition:
            query += " WHERE " + " AND ".join(condition)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        mylogger.error(e)
        return False


def delete(database: str, table: str, condition: list = None) -> bool:
    """
    从数据库中删除数据。
    Args:
        database (str): 数据库文件的路径。
        table (str): 要删除数据的表名。
        condition (list): 删除条件列表，每个条件是一个字符串。
    Returns:
        bool: 删除操作是否成功。
    """
    try:
        # 连接到数据库
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        # 构建删除语句
        query = f"DELETE FROM {table}"
        if condition:
            query += " WHERE " + " AND ".join(condition)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        mylogger.error(e)
        return False


