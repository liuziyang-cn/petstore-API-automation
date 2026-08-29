import os
import pytest

pytest.main(["-vs", "--alluredir","./report/data", "--clean-alluredir"])
os.system(f"allure generate {"./report/data"} -o {"./report/report-html"} --clean")