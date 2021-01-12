import matplotlib.pyplot as plt

fz = 10

image_list = ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10"]

host_list = [145, 178, 210, 280, 321, 406, 539, 625, 677, 720]
fre_list = [145, 184, 215, 289, 328, 416, 544, 630, 685, 725]
docker_list = [145, 195, 233, 334, 401, 541, 659, 805, 893, 1030]

plt.figure(figsize=(6, 4))

plt.plot(image_list, host_list, ':', color='k', label="Host", linewidth=0.9)
plt.plot(image_list, fre_list, '-', color='k', label="FRE", linewidth=0.9)
plt.plot(image_list, docker_list, '-.', color='k', label="Docker", linewidth=0.9)

plt.xlabel('Time', fontsize=fz)
plt.ylabel('Memory Usage(MB)', fontsize=fz)
plt.legend(loc='best', fontsize=fz)
plt.tick_params(labelsize=fz)

plt.savefig("output/mem_2.png", dpi=300, bbox_inches='tight')
plt.close()
