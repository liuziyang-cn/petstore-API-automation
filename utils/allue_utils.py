import allure

def allure_report_init(case):
    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.title(f"id:{case['id']}-{case['title']}")