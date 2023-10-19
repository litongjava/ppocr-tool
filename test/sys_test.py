import os
import sys


def get_python_home():
    return os.path.dirname(sys.executable)

def get_paddle_libs_path():
    # 获取 Python 安装路径
    python_home = get_python_home()
    # 构造 lib 路径
    paddle_libs_path = os.path.join(python_home,"Lib" ,"site-packages", "paddle", "libs")
    return paddle_libs_path

print(get_paddle_libs_path())