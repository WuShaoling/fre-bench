import matplotlib.pyplot as plt

x_label = "Features"
y_label = "Normalized Relevance"
output = "output/1.png"
fz = 8

data_list = [0.7, 0.49, 0.41, 0.2, 0.69, 0.8, 0.92, 0.98, 0.53, 0.6, 0.95, 0.99, 0.88, 0.79, 0.29, 0.24]
rects1 = plt.bar(x=[i for i in range(1, 17)], height=data_list, width=0.7, alpha=0.8, color='#BEBEBE', edgecolor='k')

plt.xlabel(x_label, fontsize=fz)
plt.ylabel(y_label, fontsize=fz)
# plt.xticks([index + 0.15 for index in x], label_list)
# plt.legend(fontsize=fz)  # 设置题注
plt.tick_params(labelsize=fz)

plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
