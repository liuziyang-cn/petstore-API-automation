import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 项目根目录
PROJECT_ROOT = os.path.dirname(current_dir)
# 常用子目录
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
JSON_DIR = PROJECT_ROOT   # JSON 文件直接放在根目录下