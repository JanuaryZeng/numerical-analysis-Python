import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def f(x):
    global string
    return eval(string)

def simpleIteration(x_data):
    x = symbols("x")
    y = string
    dify = diff(y,x)
    
    line = np.arange(-10,10,0.1)
    plt.figure(figsize=(8,8))
    plt.grid()
    plt.plot(line,line)
    plt.plot(line,f(line))

    x_data1 = f(x_data)
    plt.scatter([x_data, x_data1, x_data1], [x_data1, x_data1, f(x_data1)], color = 'b')
    plt.plot([x_data, x_data1], [x_data1, x_data1], color = 'r')
    plt.plot([x_data1, x_data1], [x_data1,f(x_data1)], color = 'r')

    while(dify.subs("x",x_data) < 1 and dify.subs("x",x_data1) < 1 and abs(x_data1-x_data) > 1e-4):

        x_data = x_data1
        x_data1 = f(x_data)
        plt.scatter([x_data, x_data1, x_data1], [x_data1, x_data1, f(x_data1)], color = 'b')
        plt.plot([x_data, x_data1], [x_data1, x_data1], color = 'r')
        plt.plot([x_data1, x_data1], [x_data1,f(x_data1)], color = 'r')
    plt.show()
    if abs(x_data1-x_data) < 1e-4:
        print("根为{}".format(x_data1))
    else:
        print("此函数牛顿法不收敛")
        

#实例公式1：(x**2 + 4*x+1)**(1/3)

while True:
    global string
    string = input("请输入符合python语言的表达式函数\n[例如x=x**2 ----> 只需要输入x**2]\n")
    line = np.arange(-10,10,0.1)
    plt.figure(figsize=(8,8))
    plt.plot(line,line)
    plt.plot(line,f(line))
    plt.grid()
    plt.show()
    n = int(input("请输入起始点值:"))
    simpleIteration(n)
    
    
    