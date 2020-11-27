import matplotlib.pyplot as plt

fz = 10

image_list = ["t1", "t2", "t3", "t4", "t5"]

host_list = [145, 210, 341, 599, 677]
fre_list = [145, 217, 348, 608, 685]
docker_list = [145, 233, 381, 680, 803]

plt.figure(figsize=(5.5, 4))

plt.plot(image_list, host_list, ':', color='k', label="Host", linewidth=0.9)
plt.plot(image_list, fre_list, '-', color='k', label="FRE", linewidth=0.9)
plt.plot(image_list, docker_list, '-.', color='k', label="Docker", linewidth=0.9)

plt.xlabel('Time', fontsize=fz)
plt.ylabel('Memory Usage(MB)', fontsize=fz)
plt.legend(loc='best', fontsize=fz)
plt.tick_params(labelsize=fz)

plt.savefig("output/mem_2.png", dpi=300, bbox_inches='tight')
plt.close()
