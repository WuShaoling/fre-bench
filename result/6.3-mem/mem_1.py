import matplotlib.pyplot as plt

label_list = ['Nodejs12', 'Python3.7', 'Ruby3', 'Java8', 'PHP8']  # 横坐标刻度显示值
list_docker = [161, 124, 152, 307, 127]  # 纵坐标值1
list_fre = [158, 119, 147, 301, 125]  # 纵坐标值2
x_label = "WebApp"
y_label = "Memory usage(MB)"
output = "output/mem_1.png"
fz = 10
x = range(len(list_docker))

plt.figure(figsize=(6, 4))

rects1 = plt.bar(x=x, height=list_docker, width=0.3, alpha=0.8, color='#BEBEBE', edgecolor='k', label="Docker")
rects2 = plt.bar(x=[i + 0.3 for i in x], height=list_fre, width=0.3, color='w', edgecolor='k', label="FRE")

plt.xlabel(x_label, fontsize=fz)
plt.ylabel(y_label, fontsize=fz)
plt.xticks([index + 0.15 for index in x], label_list)
plt.legend(fontsize=fz)  # 设置题注
plt.tick_params(labelsize=fz)

plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
