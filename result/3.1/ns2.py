import matplotlib.pyplot as plt

label_list = ['No Isolation', 'PID', 'IPC', 'Network', 'UTS', 'Mount', 'User']  # 横坐标刻度显示值
# list_docker = [828, 815, 855, 1530, 439, 452, 476]  # 纵坐标值1
list_docker = [417, 410, 427, 732, 439, 425, 411]  # 纵坐标值1
# list_fre = [18, 20, 21, 23]  # 纵坐标值2
x_label = "Concurrent Operations(512)"
y_label = "Average Latency(ms)"
output = "output/ns2.png"
fz = 10
x = range(len(list_docker))

rects1 = plt.bar(x=x, height=list_docker, width=0.5, alpha=0.8, color='#BEBEBE', edgecolor='k')
# rects2 = plt.bar(x=[i + 0.3 for i in x], height=list_fre, width=0.3, color='w', edgecolor='k', label="FRE")

# 编辑文本
# for rect in rects1:
# height = rect.get_height()
# plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom", fontsize=fz)
# for rect in rects2:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom", fontsize=fz)

plt.xlabel(x_label, fontsize=fz)
plt.ylabel(y_label, fontsize=fz)
plt.xticks([index for index in x], label_list)
# plt.ylim(0, 600)  # y轴取值范围
# plt.legend(fontsize=fz)  # 设置题注
plt.tick_params(labelsize=fz)

plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
