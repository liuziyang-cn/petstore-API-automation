import logging
import allure
import pytest
import requests

@allure.step("2.发送http请求")
def request_send(request_data):
    try:
        res = requests.request(**request_data, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Request failed: {e}")
    logging.info(f"2.返回的相应体为{res.text}")
    return res