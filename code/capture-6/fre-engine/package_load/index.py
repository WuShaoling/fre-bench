import importlib
import os
import sys
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

packages = ["django", "flask", "numpy", "pandas", "matplotlib", "setuptools", "requests", "sqlalchemy",
            "scipy", "seaborn"]
for package in packages:
    t1 = int(round(time.time() * 1e9 / 1e6))
    importlib.import_module(package)
    t2 = int(round(time.time() * 1e9 / 1e6))
    print(package + ": ", t2 - t1, "ms")

print()

for package in packages:
    t1 = int(round(time.time() * 1e9 / 1e6))
    pid = os.fork()
    if pid == 0:
        importlib.import_module(package)
        t2 = int(round(time.time() * 1e9 / 1e6))
        print(package + ": ", t2 - t1, "ms")
        sys.exit(0)
    else:
        os.waitpid(pid, 0)

'''
django:  25 ms
flask:  171 ms
numpy:  121 ms
pandas:  302 ms
matplotlib:  55 ms
setuptools:  128 ms
requests:  70 ms
sqlalchemy:  92 ms
scipy:  24 ms
seaborn:  863 ms

django:  5 ms
flask:  5 ms
numpy:  5 ms
pandas:  5 ms
matplotlib:  5 ms
setuptools:  4 ms
requests:  5 ms
sqlalchemy:  5 ms
scipy:  5 ms
seaborn:  5 ms
'''
