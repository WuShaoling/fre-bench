import matplotlib.pyplot as plt

fz = 10

x1 = [0.0005, 0.001, 0.0018, 0.002, 0.0027, 0.0031, 0.004, 0.0053, 0.0086, 0.015, 0.017]
y1 = [0.06, 0.25, 0.28, 0.32, 0.46, 0.47, 0.52, 0.57, 0.59, 0.68, 0.73]

x2 = [0.001, 0.002, 0.003, 0.004, 0.005, 0.0058, 0.0065, 0.0088, 0.010, 0.0125, 0.014, 0.0155, 0.017, 0.020]
y2 = [0.09, 0.16, 0.198, 0.27, 0.32, 0.33, 0.4, 0.41, 0.43, 0.45, 0.56, 0.58, 0.64, 0.64]

plt.figure(figsize=(5.5, 4))

plt.plot(x1, y1, '-', color='k', linewidth=0.9, marker='o', markersize=4)
plt.plot(x2, y2, '-.', color='k', linewidth=0.9, marker='*', markersize=4)

plt.xlabel('False Positive Rate', fontsize=fz)
plt.ylabel('True Positive Rate', fontsize=fz)
# plt.legend(loc='best', fontsize=fz)
plt.tick_params(labelsize=fz)

plt.xticks([0.000, 0.004, 0.008, 0.012, 0.016, 0.020])
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])

plt.savefig("output/3.png", dpi=300, bbox_inches='tight')
plt.close()
