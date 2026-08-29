import pymysql
from config.config import DATABASE, PASSWORD,USER,HOST,PORT


# 数据库连接配置（可根据环境变量动态切换，这里先写固定值）

def select_sql(sql, args=None):
    db_data = {
        "host":HOST,
        "port": PORT,
        "database": DATABASE,
        "user": USER,
        "password": PASSWORD
    }
    conn = None
    cur = None
    try:
        # 通过 ** 解包配置字典
        conn = pymysql.connect(**db_data)
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        return rows[0]
    except Exception as e:
        print(f"[SQL错误] {e}")
        raise   # 测试用例中可捕获并断言
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()