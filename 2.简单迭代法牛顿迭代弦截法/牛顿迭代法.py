import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def f(x):
    global string
    return eval(string)
    
def NewtonIteration(a):
    x = symbols("x")
    y = string
    dify = diff(y,x)
    
    dify_a = dify.subs("x",a)
    f_a = f(a)
    
    #画图
    line = np.arange(-10,10,0.1)
    plt.figure(figsize=(8,8))
    plt.grid()
    plt.plot([a, a],[0, f_a], color = 'r')
    plt.scatter([a], [f_a], color = 'b')
    
    
    while f_a > 1e-2:
        b = a - f_a / dify_a
        
        plt.plot([a, b], [f_a, 0], color = 'r')
        a = b
        f_a = f(a)
        dify_a = dify.subs("x",a)
        plt.plot([a, a], [0, f_a], color = 'r')
        plt.scatter([a], [f_a], color = 'b')
        

    plt.plot(line,f(line))
    plt.show()
    print("根为：{}".format(float(a)))
#样例函数：x**2-2*x-1
while True:
    global string
    string = input("请输入符合python语言的表达式函数\n[例如y=x**2 ----> 只需要输入x**2]\n")
    line = np.arange(-10,10,0.1)
    plt.figure(figsize=(8,8))
    plt.plot(line,f(line))
    plt.grid()
    plt.show()
    n = int(input("请输入起始点值:"))
    NewtonIteration(n)