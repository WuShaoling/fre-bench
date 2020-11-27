import csv

import matplotlib.pyplot as plt

x_label = 'Serial Operations'
y_label = 'Latency(ms)'
output = "output/create.png"
fz = 8


def read_data(file):
    csv_file = open(file, "r", encoding='utf-8')
    reader = csv.reader(csv_file)
    reader = list(map(list, zip(*reader)))

    for i in range(0, len(reader)):
        for j in range(0, len(reader[i])):
            reader[i][j] = int(reader[i][j].encode('utf-8').decode('utf-8-sig').strip())
    return reader


def draw():
    data = read_data("./merge.128.csv")
    for i in range(1, len(data)):
        for j in range(0, len(data[i])):
            data[i][j] = data[i][j] / 1000

    ax = plt.subplot()
    ax.scatter(data[0], data[1], s=5, marker='x', alpha=0.8, label='FRE')
    ax.scatter(data[0], data[2], s=4, alpha=0.5, c='r', label='FRE+Zygote')  # 改变颜色

    plt.xlabel(x_label, fontsize=fz)
    plt.ylabel(y_label, fontsize=fz)
    plt.legend(fontsize=fz)  # 设置题注
    plt.tick_params(labelsize=fz)

    plt.savefig(output, dpi=300, bbox_inches='tight')
    plt.close()


plt.figure(figsize=(5, 3))
draw()
