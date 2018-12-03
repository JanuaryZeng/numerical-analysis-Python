import matplotlib.pyplot as plt
from scipy.linalg import solve
import numpy as np

x = [0.0, 0.2, 0.4, 0.6, 0.8]
y = [0.9, 1.9, 2.8, 3.3, 4.2]

def getY(x):
    global a
    global b
    return b*np.float64(x) + a
#图中可以显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x, y, marker='o', color = 'r',label ="数据点")
plt.grid()

sum_x_2 = sum(map(lambda x:x**2, x))
sum_x = sum(x)
sum_y = sum(y)
sum_x_y = sum(map(lambda x,y:x*y,x,y))

MatA = np.array([[5,sum_x],[sum_x,sum_x_2]])
MatB = np.array([sum_y, sum_x_y])
MatX = solve(MatA,MatB)
global a
global b
a = MatX[0]
b = MatX[1]

plt.plot(x,getY(x), color='b',label= "拟合直线")
