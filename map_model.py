"""
地图模型
"""

LENGTH = 100  # 矩形地图长度 单位为米
WIDTH = 100  # 矩形地图宽度 单位为米


class Node:
    # 有短期记忆的位置坐标，能够记住上一个位置和下一个位置
    def __init__(self, x, y, _next=None, _pre=None):
        self.position = (x, y)
        self.next = _next
        self.pre = _pre


# 正方形地图，采样间隔为1米
def map1():
    head = Node(0, 0)  # 地图起点
    cur = head  # 当前位置游标
    for i in range(WIDTH-1):
        head.next = Node(0, i+1)
        pre = head
        head = head.next
        head.pre = pre
    for i in range(LENGTH-1):
        head.next = Node(i+1, WIDTH-1)
        pre = head
        head = head.next
        head.pre = pre
    for i in range(1, WIDTH):
        head.next = Node(LENGTH-1, WIDTH-1-i)
        pre = head
        head = head.next
        head.pre = pre
    for i in range(1, LENGTH-1):
        head.next = Node(LENGTH-i-1, 0)
        pre = head
        head = head.next
        head.pre = pre
    head.next = cur
    cur.pre = head
    return cur


# M = map1()
# x = []
# y = []
# while M:
#     x.append(M.position[0])
#     y.append(M.position[1])
#     M = M.next
#     if M.position == (0,0):
#         break
# from matplotlib import pyplot as plt
# plt.scatter(x,y,s=1)
# plt.show()

# 田字形地图
def map2():
    return
