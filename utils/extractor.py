import json
import logging

import allure
import jsonpath
from utils.select_sql import select_sql


#json数据提取
def extractor_json(case, al, res):
    if case["jsonExdata"]:
        with allure.step("4.json提取"):
            for key, value in json.loads(case["jsonExdata"]).items():
                value = jsonpath.jsonpath(res.json(), value)[0]
                al[key] = value
            logging.info(f"4.根据{case['jsonExdata']}提取出{al}")


#数据库数据提取
def extractor_sql(case, al):
    if case["sqlExdata"]:
        with allure.step("4.数据库提取"):
            for key, value in json.loads(case["sqlExdata"]).items():
                value = select_sql(value)
                al[key] = value
            logging.info(f"4.根据{case['sqlExdata']}提取出{al}")
