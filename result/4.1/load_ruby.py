import matplotlib.pyplot as plt

'''
rspec : 89
mime-types : 166
i18n : 57
aws-sdk-core : 550
minitest : 31
thread_safe : 22
addressable : 118
diff-lcs : 29
bundler : 80
multi_json : 18

rspec : 2
mime-types : 3
i18n : 2
aws-sdk-core : 3
minitest : 3
thread_safe : 3
addressable : 4
diff-lcs : 2
bundler : 4
multi_json : 3
'''

plt.figure(figsize=(10, 4))

label_list = ['rspec', 'mime-types', 'i18n', 'minitest',
              'thread_\nsafe', 'address\nable', 'diff-lcs', 'bundler', 'multi_json']  # 横坐标刻度显示值
list_docker = [89, 166, 57, 31, 22, 118, 29, 80, 18]  # 纵坐标值1
list_fre = [2, 3, 2, 3, 3, 4, 2, 4, 3]  # 纵坐标值2
x_label = "(b) Ruby Packages"
y_label = "Load Time(ms)"
output = "output/ruby.png"
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
