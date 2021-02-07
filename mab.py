"""
多臂老虎机问题模型
"""
import random

import numpy as np

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)


class MAB:
    def __init__(self, arms, tasks):
        # arms 为任务车集合（索引0为位置x坐标，1为y坐标，2为计算能力，3为传输速度），
        # tasks 为任务队列(绑定了位置信息，元素索引0为位置x坐标，1为y坐标，2为车载自身计算能力，3为任务数据量，
        #                                       4为任务计算强度，5为任务时延要求，6为任务重要程度)
        self.arms = arms
        self.tasks = tasks
        self.Q = np.zeros(len(arms))  # 每个臂的Q值，初始化为0，保存在列表中
        self.armCounter = np.zeros(len(arms))  # 每个臂被选择的次数，初始化为0，保存在列表中
        self.delayList = []  # 记录每次卸载的平均延迟

    def reset(self):
        self.Q = np.zeros(len(self.arms))
        self.armCounter = np.zeros(len(self.arms))
        self.delayList = []

    def getQ(self):
        return self.Q

    def getAverageDelay(self):
        average = []
        for i in range(1, len(self.delayList)):
            average.append(np.average(self.delayList[0:i]))
        return average

    def sysInit(self):
        # 初始化将第一个任务卸载到所有车辆，记录延迟和收益
        transmitDelay = self.tasks[0][3] / np.array(self.arms)[:, 3]  # 式3.6
        comDelay = self.tasks[0][3] * self.tasks[0][4] / np.array(self.arms)[:, 2]  # 式3.8
        totalDelay = transmitDelay + comDelay  # 式3.10
        self.armCounter += 1
        self.delayList.append(np.average(totalDelay))
        self.Q = np.add(self.Q, 1 / totalDelay)
        return

    def updateQ_Delay(self, arm_index, delay):
        self.armCounter[arm_index] += 1  # 指定的服务车收到卸载的次数加1
        self.Q = (self.Q * (self.armCounter - 1) + 1 / delay) / self.armCounter
        # 更新平均Q值（式3.14）：（上次卸载的Q值*历史收到卸载次数+本次延迟的倒数）/ 累计收到卸载次数
        self.delayList.append(delay)
        # 更新平均延迟（式3.11）：（上次的平均延迟*历史已处理任务总数+延迟）/ 累计计算卸载次数

    def ucb(self):
        # 本文UCB
        counter = 0
        for t in self.tasks:
            counter += 1
            transmitDelay = t[3] / np.array(self.arms)[:, 3]  # 式3.6
            comDelay = t[3] * t[4] / np.array(self.arms)[:, 2]  # 式3.8
            totalDelay = transmitDelay + comDelay  # 式3.10
            AList = self.Q + np.sqrt(2 * np.log(counter) /
                                     (self.armCounter *
                                      np.sqrt(1 + (np.array(self.arms)[:, 0] - t[0]) ** 2
                                              + (np.array(self.arms)[:, 1] - t[1]) ** 2))
                                     * min(0.25, np.var(self.Q)))  # 式3.17
            arm_index = np.argmax(AList)  # 选取式3.17计算出的最佳操作臂
            self.updateQ_Delay(arm_index, totalDelay[arm_index])  # 更新延迟和Q值

    def PriUcb(self):
        # 原始UCB
        counter = 0
        for t in self.tasks:
            counter += 1
            transmitDelay = t[3] / np.array(self.arms)[:, 3]  # 式3.6
            comDelay = t[3] * t[4] / np.array(self.arms)[:, 2]  # 式3.8
            totalDelay = transmitDelay + comDelay  # 式3.10
            AList = self.Q + np.sqrt(2 * np.log(counter) / self.armCounter)
            arm_index = np.argmax(AList)  # 选取式3.17计算出的最佳操作臂
            self.updateQ_Delay(arm_index, totalDelay[arm_index])  # 更新延迟和Q值

    def Random(self):
        delay = []
        counter = 0
        for t in self.tasks:
            counter += 1
            transmitDelay = t[3] / np.array(self.arms)[:, 3]  # 式3.6
            comDelay = t[3] * t[4] / np.array(self.arms)[:, 2]  # 式3.8
            totalDelay = transmitDelay + comDelay  # 式3.10
            arm_index = random.randint(0, len(self.arms)-1)
            delay.append(totalDelay[arm_index])
        average = [delay[0]]
        for i in range(1, len(delay)):
            average.append(np.average(delay[0:i]))
        return average
