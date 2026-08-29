import logging

import allure
import jsonpath
from utils.select_sql import select_sql


@allure.step("3.http响应结果断言")
def http_asserts(case, res):
    # http 响应断言
    if case["check"]:
        actual = jsonpath.jsonpath(res.json(), case['check'])[0]
        expected = str(case['expected'])
        logging.info(f"3.响应内容: {actual} == {expected}")
        assert actual == expected
    else:
        expected = str(case['expected'])
        logging.info(f"3.响应内容: {expected} in {res.text}")
        assert expected in res.text


def sql_asserts(case):
    # 数据库响应断言
    if case["sql_check"] and case["sql_expected"]:
        with allure.step("3.sql响应结果断言"):
            actual = select_sql(case['sql_check'])
            expected = case['sql_expected']
            logging.info(f"3.数据库断言: {actual} == {expected}")
            assert actual == expected
