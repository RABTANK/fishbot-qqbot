import os
import sqlite3


def select(database:str,target:str='*',table:str=None,condition:list=None):
    """
    args:
        database:数据库路径
        target:目标
        table:表
        condition:条件列表
    return:
        res:查询结果
    """
    sql="select {} from {} ".format(target,table)
    if condition:
        sql+="where {}".format(" and ".join(condition))
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res


dbpath=os.path.join(os.getcwd(),"functions/fish-game/res/text.db")
print(dbpath)
print(select(dbpath,"content","text",["id=100001"]))