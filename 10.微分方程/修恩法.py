import matplotlib.pyplot as plt
import numpy as np


"""
修恩法
"""
def compute(func, x):
        y_deri = 0
        for i,j in enumerate(func[::-1]):
            y_deri += (x**i)*j
        return y_deri

def euler(fc, x0, y0, lenth, start, end):       #定义Euler算法的过程
    n = int((end-start)/lenth)
    x_list = [x0]
    y_list = [y0]
    for i in range(n):
        x_ = x_list[-1]
        y_ = y_list[-1]
        y_fc0 = compute(fc,x_)
        y_fc1 = compute(fc,x_ + lenth)
        y_fc=(y_fc0 + y_fc1)/2
        x_ += lenth
        y_ += lenth * y_fc
        x_list.append(x_)
        y_list.append(y_)
    return x_list,y_list
    
func = [-0.4, 3, -5, 6, 1]
fc = [-1.6, 9, -10, 6] #3阶方程
x0=0
y0=1
lenth=0.5
x_start = -1
x_end = 5
#可以显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False
print("1607094240 曾祥玖")
x, y = euler(fc, x0, y0, lenth, x_start, x_end)
plt.figure(figsize=(10,10))
plt.xlabel('X')
plt.ylabel('Y')
plt.title("修恩法求解微分方程$y=f(x)=-0.4x^4+3x^3-5x^2+6x+1$结果")
plt.plot(x,y,c='blue',label='欧拉法')
x = np.arange(x_start,x_end+1.1,0.1)
plt.plot(x,[compute(func,i) for i in x],c='black',label='原函数')
plt.legend(['修恩法','原函数'])
plt.grid()
plt.show()