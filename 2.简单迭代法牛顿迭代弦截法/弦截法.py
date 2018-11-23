import numpy as np
import matplotlib.pyplot as plt

def f(x):
    global string
    return eval(string)

def ChordCut(a, b):
    f_a = f(a)
    f_b = f(b)
    k = (f_b - f_a)/(b - a)
    c = a - f_a / k
    
    line = np.arange(-10,10,0.1)
    plt.figure(figsize=(8,8))
    plt.grid()
    plt.plot([a, c],[f_a, 0], color = 'r')
    plt.scatter([a, b], [f_a, f_b], color = 'g')
    
    while f_a > 1e-8:
        a = b
        b = c
        f_a = f(a)
        f_b = f(b)
        k = (f_b - f_a)/(b - a)
        c = a - f_a / k
        plt.plot([a, c],[f_a, 0], color = 'r')
        plt.scatter([a, b], [f_a, f_b], color = 'g')
    
    plt.plot(line,f(line))
    plt.show()
    print("根为：{}".format(float(a)))
#样例函数：  x**2-2*x-1  
while True:
    global string
    string = input("请输入符合python语言的表达式函数\n[例如y=x**2 ----> 只需要输入x**2]\n")
    line = np.arange(-10,10,0.1)
    plt.figure(figsize=(8,8))
    plt.plot(line,f(line))
    plt.grid()
    plt.show()
    print("请输入起点1 和起点2[起点1<起点2]")
    a = int(input("请输入起点1:"))
    b = int(input("请输入起点2:"))

    ChordCut(b, a)