"""
主程序入口
"""
import matplotlib

from mab import MAB
from vehicle_model import taskCar, serverCar
from map_model import map1
from matplotlib import pyplot as plt

matplotlib.rcParams['font.family']='SimHei'

def chapter3():
    M = map1()  # 新建地图对象
    positions = []  # 地图坐标
    while M:
        positions.append([M.position[0], M.position[1]])
        M = M.next
        if M.position == (0, 0):
            break
    server = [[22, 0, 150, 300],
              [0, 33, 150, 200],
              [99, 35, 200, 200],
              [0, 57, 200, 800],
              [0, 80, 250, 500],
              [47, 99, 800, 100],
              [0, 9, 250, 100],
              [34, 99, 600, 100],
              [99, 92, 100, 150],
              [0, 98, 250, 200]]# 初始化服务车对象
    tasks = []  # 初始化任务车对象
    for i in range(3000):
        tasks.append(taskCar(positions))

    mab = MAB(server, tasks)
    mab.sysInit()
    mab.ucb()
    delay = mab.getAverageDelay()  # 本文UCB
    delay1 = mab.Random()  # 随机
    mab.reset()
    mab.sysInit()
    mab.PriUcb()
    delay2 = mab.getAverageDelay()  # 原始UCB
    # delay1.append(delay1[-1])
    x = [i for i in range(1, len(delay)+1)]
    plt.figure(figsize=(9, 7), dpi=300)
    plt.plot(x, delay, linestyle="--", label="本文算法")
    plt.plot(x, delay1, linestyle="-.", label="随机卸载")
    plt.plot(x, delay2, linestyle=":", label="原始UCB")
    fontsize = 20
    plt.legend(fontsize=fontsize)
    plt.xlabel('迭代次数', fontsize=fontsize)
    plt.ylabel('平均延迟（ms）', fontsize=fontsize)
    plt.tick_params(labelsize=fontsize)
    plt.show()


if __name__ == "__main__":
    chapter3()
