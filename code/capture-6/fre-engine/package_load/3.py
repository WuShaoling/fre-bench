import importlib
import time

''' 测试包加载的时间
执行流程

1. 使用 docker python:3.7 环境
docker run -it -v $PWD:/root python:3.7 bash

2. 安装依赖包
pip3 install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com \
    django flask numpy pandas matplotlib setuptools requests sqlalchemy seaborn scipy

3. 执行测试脚本
python /root/package_load_time.py
'''
#
# t1 = int(round(time.time() * 1e9 / 1e6))
# importlib.import_module("numpy")
# t2 = int(round(time.time() * 1e9 / 1e6))
# print("numpy" + ": ", t2 - t1, "ms")

# 先导入scipy
t1 = int(round(time.time() * 1e9 / 1e6))
importlib.import_module("scipy")
t2 = int(round(time.time() * 1e9 / 1e6))
print("scipy" + ": ", t2 - t1, "ms")

# 再导入numpy
t1 = int(round(time.time() * 1e9 / 1e6))
importlib.import_module("numpy")
t2 = int(round(time.time() * 1e9 / 1e6))
print("numpy" + ": ", t2 - t1, "ms")

# # scipy -> numpy
#
# pid = os.fork()
# if pid == 0:
#     # 直接导入 numpy
#     t1 = int(round(time.time() * 1e9 / 1e6))
#     importlib.import_module("numpy")
#     t2 = int(round(time.time() * 1e9 / 1e6))
#     print("numpy" + ": ", t2 - t1, "ms")
#     sys.exit(0)
# else:
#     os.waitpid(pid, 0)
#
# pid = os.fork()
# if pid == 0:
#     # 先导入scipy
#     t1 = int(round(time.time() * 1e9 / 1e6))
#     importlib.import_module("scipy")
#     t2 = int(round(time.time() * 1e9 / 1e6))
#     print("scipy" + ": ", t2 - t1, "ms")
#
#     # 再导入numpy
#     t1 = int(round(time.time() * 1e9 / 1e6))
#     importlib.import_module("numpy")
#     t2 = int(round(time.time() * 1e9 / 1e6))
#     print("numpy" + ": ", t2 - t1, "ms")
#
#     sys.exit(0)
# else:
#     os.waitpid(pid, 0)
