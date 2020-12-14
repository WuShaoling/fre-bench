import matplotlib.pyplot as plt

'''
django:  19 ms
flask:  209 ms
numpy:  120 ms
pandas:  279 ms
matplotlib:  56 ms
setuptools:  124 ms
requests:  75 ms
sqlalchemy:  102 ms
scipy:  24 ms
seaborn:  863 ms

django:  3 ms
flask:  4 ms
numpy:  4 ms
pandas:  4 ms
matplotlib:  5 ms
setuptools:  4 ms
requests:  4 ms
sqlalchemy:  4 ms
scipy:  4 ms
seaborn:  4 ms
'''

plt.figure(figsize=(10, 4))

label_list = ['django', 'flask', 'numpy', 'pandas', 'matplotlib', 'scipy', 'setuptools', 'requests',
              'sqlalchemy']  # 横坐标刻度显示值
list_docker = [19, 209, 120, 279, 56, 24, 124, 75, 102]  # 纵坐标值1
list_fre = [3, 4, 4, 4, 5, 4, 4, 4, 5]  # 纵坐标值2
x_label = "(a) Python Packages"
y_label = "Load Time(ms)"
output = "output/python.png"
fz = 10
x = range(len(list_docker))

rects1 = plt.bar(x=x, height=list_docker, width=0.3, alpha=0.8, color='#BEBEBE', edgecolor='k', label="Import")
rects2 = plt.bar(x=[i + 0.3 for i in x], height=list_fre, width=0.3, color='w', edgecolor='k', label="Import by zygote")

# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom", fontsize=fz)
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom", fontsize=fz)

plt.xlabel(x_label, fontsize=fz)
plt.ylabel(y_label, fontsize=fz)
plt.xticks([index + 0.15 for index in x], label_list)
plt.legend(fontsize=fz)  # 设置题注
plt.tick_params(labelsize=fz)

plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
