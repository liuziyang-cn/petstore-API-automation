import os
import sys
import pytest

# sys.path 引导：确保项目根目录在任何 import 之前进入搜索路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.config import HOST, PORT, DATABASE, USER, PASSWORD, SQL_DELETE


#如果要销毁数据库多余内容
@pytest.fixture(scope="session")
def destroy_data():
    yield
    db_data = {
        "host": HOST,
        "port": PORT,
        "database": DATABASE,
        "user": USER,
        "password": PASSWORD,
        "autocommit": True
    }
    conn = None
    cur = None
    try:
        conn = pymysql.connect(**db_data)
        cur = conn.cursor()
        for sql in SQL_DELETE:
            cur.execute(sql)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()