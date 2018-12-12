import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

def func(x):
    return 0.5*x**5+x**4+x**3-5*x**2-4*x+1
    
def f(a,b,c,x):
    return a*x**2+b*x+c

#n+1个点有2n-1个未知数 有2n-1个

def SecondaryMethod(n):
    global xList
    num = n*3
    X = np.zeros((num,num))
    Y = np.zeros((num))
    b = 0
    #第几个点 在b==0的时候指向下一个点
    j = 0
    #第几个方程 在b==1的时候指到下一个方程
    k = 0
    #i是带入点能得到的方程
    for i in range(2*n):
        yNum = func(xList[j])
        xNum = xList[j]
        #确定a b c的位置
        number = 3*k
        Y[i] = yNum
        X[i][number] = xNum**2
        X[i][number+1] = xNum
        X[i][number+2] = 1
        if b==0:
            b = 1
            j += 1
        elif b==1:
            b = 0
            k += 1
    #第几个方程
    k = 0
    #第几个点
    j = 1
    #i是得到导数相等得到的方程
    for i in range(2*n,num-1,1):
        number1 = 3*k
        number2 = 3*(k+1)
        X[i][number1] = 2*xList[j]
        X[i][number1+1] = 1
        X[i][number2] = -2*xList[j]
        X[i][number2+1] = -1
        j += 1
        k += 1
    X[num-1][0] = 1
    Lambda = solve(X,Y)
#    print(X)
#    print(Y)
#    print(Lambda)
    return Lambda

def draw(Lambda,n):
    global xList
    plt.figure(figsize=(10,10))
    line = np.arange(xList[0],xList[n]+0.01,0.01)
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(line,func(line),color = 'b',label = '原函数')
    
    plt.grid()
    for i in range(n):
        x1 = xList[i]
        x2 = xList[i+1]
        line = np.arange(x1,x2+0.01,0.01)
        num = i*3
        a = Lambda[num]
        b = Lambda[num+1]
        c = Lambda[num+2]
        plt.plot(line,f(a,b,c,line),color='g',label = '拟合函数')
    plt.legend(['原函数','拟合函数'])
    plt.title('二次样条法')
    
    for i in range(n+1):
        plt.scatter(xList[i],func(xList[i]),color = 'r')

global xList
n = int(input('请输入点的个数:'))
xList = list()
for i in range(n):
    num = np.random.uniform(-2.5, 3)
    xList.append(num)
#xList = [-1,0,1,2]
xList.sort()
n = len(xList)-1
Lambda = SecondaryMethod(n)
draw(Lambda,n)