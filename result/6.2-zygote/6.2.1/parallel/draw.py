import csv
import math

import matplotlib.pyplot as plt

import numpy as np

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
    matrix = read_data("data_set/merge.64.csv")

    for i in range(1, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j] / 1000
            # matrix[i][j] = math.sqrt(matrix[i][j])
            # matrix[i][j] = np.log2(matrix[i][j])

    plt.plot(matrix[0], matrix[2], '-.', color='k', label="FRE", linewidth=0.9)
    plt.plot(matrix[0], matrix[1], ':', color='k', label="FRE+Zygote", linewidth=0.9)
    plt.plot(matrix[0], matrix[3], '-', color='k', label="Docker", linewidth=0.9)

    plt.legend(loc='best', fontsize=fz)
    plt.xlabel('Concurrent Operations', fontsize=fz)
    plt.ylabel('Latency(ms)', fontsize=fz)
    plt.xticks([0, 16, 32, 48, 64])
    plt.tick_params(labelsize=fz)


# plt.figure(figsize=(5, 3.5))
draw()
plt.savefig("output/create.png", dpi=300, bbox_inches='tight')
plt.close()
