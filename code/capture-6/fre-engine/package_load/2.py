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

for i in range(0, len(packages)):
    pid = os.fork()
    if pid == 0:
        t1 = int(round(time.time() * 1e9 / 1e6))
        importlib.import_module(packages[i])
        t2 = int(round(time.time() * 1e9 / 1e6))
        print(packages[i] + ": ", t2 - t1, "ms")
        sys.exit(0)
    else:
        os.waitpid(pid, 0)

'''
django:  24 ms
flask:  189 ms
numpy:  156 ms
pandas:  427 ms
matplotlib:  222 ms
setuptools:  223 ms
requests:  143 ms
sqlalchemy:  142 ms
scipy:  186 ms
seaborn:  1086 ms

django:  26 ms
flask:  198 ms
numpy:  168 ms
pandas:  521 ms
matplotlib:  302 ms
setuptools:  213 ms
requests:  162 ms
sqlalchemy:  163 ms
scipy:  205 ms
seaborn:  1211 ms

django:  27 ms
flask:  192 ms
numpy:  157 ms
pandas:  464 ms
matplotlib:  226 ms
setuptools:  209 ms
requests:  142 ms
sqlalchemy:  150 ms
scipy:  181 ms
seaborn:  1122 ms
'''
