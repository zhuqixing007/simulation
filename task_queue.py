"""
任务队列
"""
import numpy as np
from task_generator import task_generator


def priority(T):
    # 计算任务优先级
    M = np.array(T)  # 任务集转化为矩阵
    S = np.sum(M, axis=0)  # 对矩阵列求和
    P = []  # 概率矩阵
    for t in T:
        P.append([t[0] / S[0], t[1] / S[1],
                  t[2] / S[2], t[3] / S[3]])
    P = np.array(P)
    H = -np.sum(np.multiply(P, np.log(P)), axis=0) / np.log(np.shape(P)[0])  # 计算每一列的熵值
    W = []  # 权重矩阵
    for h in H:
        W.append((1 - h) / (4 - np.sum(H)))
    V = P @ np.transpose(W)  # 优先级
    return V


def task_queue(V, T):
    # 根据优先级创建任务队列
    print(V)
    print(T)
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if V[i] < V[j]:
                temp1 = V[i]
                V[i] = V[j]
                V[j] = temp1
                temp2 = T[i]
                T[i] = T[j]
                T[j] = temp2
    print(V)
    print(T)
    return T
