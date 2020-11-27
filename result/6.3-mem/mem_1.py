import matplotlib.pyplot as plt

label_list = ['Nodejs8', 'Python2.7', 'Python3', 'Java8', 'PHP5.6']  # 横坐标刻度显示值
list_docker = [161, 124, 132, 307, 127]  # 纵坐标值1
list_fre = [155, 109, 117, 282, 120]  # 纵坐标值2
x_label = "WebApp"
y_label = "Memory usage(MB)"
output = "output/mem_1.png"
fz = 10
x = range(len(list_docker))

rects1 = plt.bar(x=x, height=list_docker, width=0.3, alpha=0.8, color='#BEBEBE', edgecolor='k', label="Docker")
rects2 = plt.bar(x=[i + 0.3 for i in x], height=list_fre, width=0.3, color='w', edgecolor='k', label="FRE")

plt.xlabel(x_label, fontsize=fz)
plt.ylabel(y_label, fontsize=fz)
plt.xticks([index + 0.15 for index in x], label_list)
plt.legend(fontsize=fz)  # 设置题注
plt.tick_params(labelsize=fz)

plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
