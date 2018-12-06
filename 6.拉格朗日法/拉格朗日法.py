import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return 0.5*x**5+x**4+x**3-5*x**2-4*x+1
    
def Lagrangian(x):
    global xList
    length = len(xList)
    number = 0
    for i in range(length):
        temp = 1
        for j in range(length):
            if i == j:
                continue
            numb = (x - xList[j])/(xList[i] - xList[j])
            temp *= numb
        temp *= func(xList[i])
        number += temp
    return number
    
global xList
xList = list()

n = int(input('请输入点的个数:'))
for i in range(n):
    num = np.random.uniform(-2.5, 3)
    xList.append(num)

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False
line = np.arange(-3,3.5,0.1)
plt.figure(figsize=(8,18))
plt.subplot(3,1,1)
plt.plot(line, func(line), color = 'g')
plt.scatter(np.array(xList),func(np.array(xList)),color = 'r')
plt.grid()
plt.title('原函数和点')
plt.subplot(3,1,2)
plt.plot(line, Lagrangian(line), color = 'b')
plt.scatter(np.array(xList),func(np.array(xList)),color = 'r')
plt.grid()
plt.title('拟合函数')
plt.subplot(3,1,3)
plt.plot(line, Lagrangian(line), color = 'b')
plt.plot(line, func(line), color = 'g')
plt.scatter(np.array(xList),func(np.array(xList)),color = 'r')
plt.grid()
plt.title('两曲线重合度')
'''
最好效果为6个点！
'''