"""
车辆生成模块
"""

import random
from task_generator import task_generator


def taskCar(mapPositions):
    position = random.choice(mapPositions)
    task = task_generator()
    ability = 0.5*task[1]  # 自身计算能力定义为计算强度的一半
    return [position[0], position[1], ability, task[0], task[1], task[2], task[3]]


def serverCar(mapPositions):
    position = random.choice(mapPositions)  # 位置
    ability = random.choice([100, 150, 200, 250, 800])  # 计算能力
    band = random.choice([100, 150, 200, 250, 800])  # 带宽
    return [position[0], position[1], ability, band]
