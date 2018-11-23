chiimport matplotlib.pyplot as plt
import numpy as np

#设置的函数
global string
def f(x):
    global string
    return eval(string)

#二分递归法
def ordnaryDeal(left, right):
    numb1 = f(left)
    numb2 = f(right)
    mid = (right + left)/2
    numb3 = f(mid)
    
    if numb1 * numb2 > 0:
        print("此范围没有实数根！！")
        return
    elif temp(numb1, numb2):
        return
    elif right - left < 1e-8:
        print("根的范围为:[{},{}]".format(left, right))
        return
    elif numb1 * numb3 < 0:
        ordnaryDeal(left, mid)
    elif numb2 * numb3 < 0:
        ordnaryDeal(mid, right)
    elif numb3 == 0:
        print("根为:{}".format(mid))
        return
#试位循环法
def findDeal(left, right):
    numb1 = f(left)
    numb2 = f(right)
    if numb1 * numb2 > 0:
        print("此范围没有实数根！！")
        return
    elif temp(numb1, numb2):
        return
        
    i = 0
    b = True
    while(right - left > 1e-3):
        i = i + 1
        #最高150次循环，防止进入死循环
        if i >150:
            break
        numb1 = f(left)
        numb2 = f(right)
        if temp(numb1, numb2):
            b = False
            return
        
        x1 = (abs(numb1)/abs(numb2)*(right-left))/(abs(numb1)/abs(numb2) + 1)
        numb3 = f(left + x1)
        if numb1 * numb3 < 0:
            right = left + x1
        elif numb2 * numb3 < 0:
            left = left + x1
        elif numb3 == 0:
            print("根为:{}".format(left + x1))
            break
    if b:
        print("根的范围为:[{},{}]".format(left, right))

#判别函数
def temp(numb1, numb2):
    if numb1 == 0 and numb2 == 0 and numb1 != numb2:
        print("根为:{}和{}".format(numb1,numb2))
    elif numb1 == 0 and numb2 ==0 and numb1 == numb2:
        print("根为:{}".format(numb1))
        return True
    elif numb1 == 0:
        print("根为:{}".format(numb1))
        return True
    elif numb2 == 0:
        print("根为:{}".format(numb2))
        return True



while True:
    global string 

    string = input('请输入符合python语言的表达式函数\n[例如y=x**2 ----> 只需要输入x**2]\n:')
    line = np.arange(-4, 4, 0.01)

    plt.plot(line, f(line))
    plt.grid()
    plt.show()
    
    print("\n[1]:二分法\n[2]:试位法\n[3]:调整图像范围\n")

    judge = int(input())
    if judge == 3:
        boolean = True
    else:
        boolean = False
    while boolean:
        L = float(input("请输入图像左边界:"))
        R = float(input("请输入图像右边界:"))
        line = np.arange(L, R, 0.01)
        plt.plot(line, f(line))
        plt.grid()
        plt.show()
        Booler = int(input("[1]:调整图像边界\n[elseInteger]:进行计算\n"))
        if Booler != 1:
            print("\n[1]:二分法\n[2]:试位法\n")
            judge = int(input())
            break
    
    left = float(input("请输入左边界:"))
    right= float(input("请输入右边界:"))
    
    if judge == 1:
        ordnaryDeal(left, right)
    elif judge == 2:
        findDeal(left, right)

    
    

    
    
