import csv

import matplotlib.pyplot as plt

output = "output/overlay.png"
fz = 10


def read_data(file):
    csv_file = open(file, "r", encoding='utf-8')
    reader = csv.reader(csv_file)
    reader = list(map(list, zip(*reader)))

    for i in range(0, len(reader)):
        for j in range(0, len(reader[i])):
            reader[i][j] = int(reader[i][j].encode('utf-8').decode('utf-8-sig').strip())
    return reader


def draw_a():
    plt.subplot(1, 2, 1)
    label_list = ['32', '64', '128', '256', '512']
    list_mkdir = [4.247, 6.598, 12.260, 21.244, 38.016]
    list_mount = [0.623, 0.764, 0.699, 0.669, 0.835]
    total = [4.247 + 0.623, 6.598 + 0.764, 12.260 + 0.699, 21.244 + 0.669, 38.016 + 0.835]

    x_label = '(a) Concurrent Operations'
    y_label = 'Latency(ms)'

    x = range(len(list_mkdir))

    plt.bar(x=x, height=list_mkdir, width=0.5, alpha=0.8, color='#BEBEBE', edgecolor='k', label="mkdir")
    plt.bar(x=x, height=list_mount, bottom=list_mkdir, width=0.5, color='w', edgecolor='k', label="mount")

    for (a, b) in zip(x, total):
        plt.text(a, b + 0.1, "%.2f" % b, ha='center', va='bottom', fontsize=fz)

    # for (a, b) in zip(x, list_mkdir):
    #     plt.text(a, b - 3, "%.2f" % b, ha='center', va='bottom', fontsize=fz)

    plt.xlabel(x_label, fontsize=fz)
    plt.ylabel(y_label, fontsize=fz)
    plt.xticks(x, label_list)
    plt.legend(fontsize=fz)  # 设置题注
    plt.tick_params(labelsize=fz)


# def draw_b():
#     plt.subplot(1, 2, 2)
#     label_list = ['32', '64', '128', '256', '512']
#     create = [4.247 + 0.623, 6.598 + 0.764, 12.260 + 0.699, 21.244 + 0.669, 38.016 + 0.835]
#     pool = [0.93, 1.12, 1.39, 1.57, 1.66]
#
#     x_label = 'Concurrent Operations'
#     y_label = 'Latency(ms)'
#
#     x = range(len(create))
#
#     plt.bar(x=x, height=create, width=0.3, alpha=0.8, color='#BEBEBE', edgecolor='k', label="create")
#     plt.bar(x=[i + 0.3 for i in x], height=pool, width=0.3, color='w', edgecolor='k', label="pool")
#
#     # for (a, b) in zip(x, create):
#     #     plt.text(a, b + 0.1, "%.2f" % b, ha='center', va='bottom', fontsize=fz)
#
#     # for (a, b) in zip(x, list_mkdir):
#     #     plt.text(a, b - 3, "%.2f" % b, ha='center', va='bottom', fontsize=fz)
#
#     plt.xlabel(x_label, fontsize=fz)
#     plt.ylabel(y_label, fontsize=fz)
#     plt.xticks([index + 0.15 for index in x], label_list)
#     plt.legend(fontsize=fz)  # 设置题注
#     plt.tick_params(labelsize=fz)


def draw_c():
    plt.subplot(1, 2, 2)
    matrix = read_data("data_set/overlay_512.b.csv")

    for i in range(1, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j] / 1000

    x = []
    for i in range(0, len(matrix[0])):
        x.append(i)

    plt.plot(x, matrix[3], '-', color='k', label="pool", linewidth=0.9)
    plt.plot(x, matrix[4], ':', color='k', label="create", linewidth=0.9)

    plt.legend(loc='best', fontsize=fz)
    plt.xlabel('(b) Concurrent Operations(512)', fontsize=fz)
    plt.ylabel('Latency(ms)', fontsize=fz)
    plt.xticks([0, 128, 256, 384, 512])
    plt.tick_params(labelsize=fz)


plt.figure(figsize=(11, 3.5))
draw_a()
draw_c()
plt.savefig(output, dpi=300, bbox_inches='tight')
plt.close()
