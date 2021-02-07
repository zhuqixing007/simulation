"""
计算任务生成模块
"""

import random

MAX_DATA_SIZE = 300  # 任务最大数据量  bit
MAX_COM_INTENSITY = 300  # 任务最大计算强度 cycle/bit
MAX_DELAY = 200  # 任务最大延迟 ms
MAX_PRIORITY = 1  # 任务最大重要程度


def task_generator():
    size = random.randint(100, MAX_DATA_SIZE)
    intensity = random.randint(10, MAX_COM_INTENSITY)
    delay = random.randint(10, MAX_DELAY)
    priority = random.uniform(0, MAX_PRIORITY)
    t = [size, intensity, delay, priority]
    return t


# for i in range(10):
#     print(task_generator())
