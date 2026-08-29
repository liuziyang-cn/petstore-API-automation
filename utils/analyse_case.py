import json
import logging
import allure
from config.config import BASE_URL


@allure.step("1.解析请求数据")
def analyse_case(case):
    method = case["method"]
    url = BASE_URL + case["url"]
    params = json.loads(case["params"]) if case["params"] is not None else None
    data = json.loads(case["data"]) if case["data"] is not None else None
    json_data = json.loads(case["json"]) if case["json"] is not None else None
    files = case['files'] if case["files"] is not None else None
    headers = json.loads(case["headers"]) if case["headers"] is not None else None

    request_data = {
        "method": method,
        "url": url,
        "params": params,
        "data": data,
        "json": json_data,
        "files": files,
        "headers": headers
    }
    logging.info(f"1.解析的请求数据为{request_data}")
    return request_data