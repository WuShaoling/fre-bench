import matplotlib.pyplot as plt

x_label = "Components"
y_label = "Percentage"
output = "output/2.png"
fz = 8

data_list = [0.88, 0.09, 0.03, 0.02, 0.01, 0.009]
rects1 = plt.bar(x=[i for i in range(1, len(data_list) + 1)], height=data_list, width=0.7, alpha=0.8, color='#BEBEBE',
                 edgecolor='k')

plt.xlabel(x_label, fontsize=fz)
plt.ylabel(y_label, fontsize=fz)
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# plt.xticks([index + 0.15 for index in x], label_list)
# plt.legend(fontsize=fz)  # 设置题注
plt.tick_params(labelsize=fz)

plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
