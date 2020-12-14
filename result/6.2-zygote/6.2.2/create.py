import matplotlib.pyplot as plt

label_list = ['django', 'flask', 'numpy', 'pandas', 'matplotlib', 'setuptools', 'requests', 'sqlalchemy']
list_fre = [96, 945, 439, 1064, 490, 1292, 675, 501]  # 纵坐标值1
list_zygote = [10, 13, 13, 14, 14, 11, 12, 13]  # 纵坐标值2

x_label = "Package"
y_label = "Latency(ms)"
output = "output/create.png"
fz = 8
x = range(len(list_fre))

rects1 = plt.bar(x=x, height=list_fre, width=0.3, alpha=0.8, color='#BEBEBE', edgecolor='k', label="FRE")
rects2 = plt.bar(x=[i + 0.3 for i in x], height=list_zygote, width=0.3, color='w', edgecolor='k', label="FRE+Zygote")

# 编辑文本
# for rect in rects1:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom", fontsize=fz)
# for rect in rects2:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom", fontsize=fz)

plt.xlabel(x_label, fontsize=fz)
plt.ylabel(y_label, fontsize=fz)
plt.xticks([index + 0.15 for index in x], label_list)
plt.legend(fontsize=fz)  # 设置题注
plt.tick_params(labelsize=fz)

plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
