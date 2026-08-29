# Pet Community API 接口自动化测试框架

基于 Python + Requests 进行接口自动化测试。

## 技术栈

- Python 3.11+
- Requests（HTTP 请求）
- pytest（测试框架）
- Allure（测试报告）
- openpyxl（Excel 数据驱动）
- pymysql（数据库断言）
- jinja2（用例间变量传递）

## 项目结构

```
petstore-api-automation/
├── config/
│   └── config.py          # 环境地址、数据库、Excel 配置
├── data/
│   └── Petstore.xlsx      # 测试用例数据（97 条）
├── scripts/
│   └── test_runner.py     # 测试入口，参数化执行
├── utils/
│   ├── analyse_case.py    # 请求解析
│   ├── asserts.py         # HTTP + 数据库双断言
│   ├── excel_utils.py     # Excel 读取
│   ├── extractor.py       # JSON/数据库数据提取
│   ├── request_send.py    # 统一请求封装
│   ├── select_sql.py      # 数据库查询
│   ├── allue_utils.py     # Allure 动态标签
│   └── path_config.py     # 路径配置
├── conftest.py            # sys.path 引导 + session 级 fixture
├── pytest.ini             # pytest 配置
├── run.py                 # 一键执行 + 生成 Allure 报告
└── requirements.txt
```

## 核心设计

- **Excel 数据驱动**：97 条用例覆盖 Pet/Store/User 全部模块，含正常、异常、边界、兼容性场景
- **jinja2 模板渲染**：用例间变量传递（登录提取 session → 后续用例鉴权引用）
- **双重断言**：HTTP 响应断言（jsonpath 提取）+ 数据库断言（pymysql 查库校验）
- **统一请求封装**：超时控制 + 异常捕获 + 全链路日志

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 安装 Allure 命令行（需 Java 环境）
# Windows: scoop install allure  或  choco install allure

# 执行测试
python run.py

# 查看报告
allure open ./report/report-html
```

## 用例覆盖

| 模块 | 用例数 | 场景 |
|------|--------|------|
| 登录/登出 | 5 | 正常登录、密码错误、用户名不存在、空值、登出 |
| 宠物管理 | 34 | 新增/更新/查询/删除/表单更新/上传图片 |
| 订单管理 | 17 | 下单/查询/删除，含边界值与异常 ID |
| 用户管理 | 27 | 注册/批量创建/查询/更新/删除 |
| 库存查询 | 2 | 正常查询、缺 api_key |
| **合计** | **97** | |