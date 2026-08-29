import logging
import os.path
from jinja2 import Template
from config.config import EXCEL_FILE, SHEET_NAME
from utils.analyse_case import analyse_case
from utils.asserts import http_asserts, sql_asserts
from utils.extractor import extractor_json, extractor_sql
from utils.request_send import request_send
import pytest
from utils.allue_utils import allure_report_init
from utils.excel_utils import data_load
from utils.path_config import DATA_DIR


class Testrunner:

    # 全局字典，用于用例间变量传递
    all = {}

    @pytest.mark.parametrize("case", data_load(os.path.join(DATA_DIR, EXCEL_FILE), SHEET_NAME))
    def test_case(self, case):
        # jinja2 模板渲染，实现用例间变量引用
        case = eval(Template(str(case)).render(self.all))

        # allure 初始化
        allure_report_init(case)
        logging.info(f"{case['id']}-{case['feature']}-{case['story']}-{case['title']}")

        # 发起请求得到结果
        res = request_send(analyse_case(case))
        # 处理 http 断言
        http_asserts(case, res)
        # 处理数据库断言
        sql_asserts(case)
        # json 数据提取
        extractor_json(case, self.all, res)
        # 数据库数据提取
        extractor_sql(case, self.all)
