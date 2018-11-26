import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

def getB(a, u, v):
    global n
    aCopy = a.copy()
    aCopy.reverse()
    b = list()
    
    b0 = aCopy[0]
    b.append(b0)
    b1 = aCopy[1] - u*b0
    b.append(b1)
    i = 2
    while i <= n:
        bi = aCopy[i] - u*b[i-1] - v*b[i-2]
        b.append(bi)
        i = i + 1
    r0 = b[n-1]
    r1 = b[n] + u*b[n-1]
#    print("a:\n{}".format(aCopy))
#    print("b:\n{}".format(b))
    b.reverse()
    return b, r0, r1
    
    
def getC(b, u, v):
    global n
    bCopy = b.copy()
    bCopy.reverse()
    c = list()
    
    c0 = bCopy[0]
    c.append(c0)
    c1 = bCopy[1] - u*c0
    c.append(c1)
    i = 2
    while i <= n-2:
        ci = bCopy[i] - u*c[i-1] - v*c[i-2]
        c.append(ci)
        i = i + 1
    s0 = c[n-3]
    s1 = c[n-2] + u*c[n-3]
#    print("c:\n{}".format(c))
    c.reverse()
    return c, s0, s1
    
    

def BairstowIteration(a):
    global n
    F = np.poly1d(a)
    gen = list()
    
    line = np.arange(-10,10,0.1)
    plt.figure(figsize=(8,8))
    plt.plot(line,np.polyval(F,line))
    plt.grid()
    plt.show()
    
    while n > 2:
        u, v = -1.6, 1.3
        dertU = 100
        dertV = 100
        
        while abs(dertU) > 1e-8 and abs(dertV) > 1e-8:
#            print("++++++++++++++++++")
#            print("a:{}".format(a))
            b, r0, r1 = getB(a, u, v)
            c, s0, s1 = getC(b, u, v)
            
            m1 = -s0
            m2 = -s1
            n1 = u*s0 - s1
            n2 = v*s0

            matA = np.array([[n1,m1],[n2,m2]])
            matB = np.array([-r0, -r1])
            matX = solve(matA,matB)
            
            dertU = matX[0]
            dertV = matX[1]
#            print("dertU:{}".format(dertU))
#            print("dertV:{}".format(dertV))
            u = u + dertU
            v = v + dertV
        
        Mat = [v,u,1]
        F1 = np.poly1d(Mat)
#        print("Mat:\n{}".format(Mat))
        n = n - 2
        genTemp = np.roots(Mat)
        gen.append(genTemp[0])
        gen.append(genTemp[1])

        F, Q = F / F1
        a = np.array(F)
        a = list(a)

    genTemp = np.roots(a)

    if len(genTemp) == 1:
        gen.append(genTemp[0])
    elif len(genTemp) == 2:
        gen.append(genTemp[0])
        gen.append(genTemp[1])
    print("根为:\n{}".format(gen))
    
while True:
    global n, m
    n = int(input("请输入多项式的阶数(输入0:exit): "))
    if n == 0:
        break;
    a  = list()
    i = 0
    while i <= n:
        a.append(float(input("请输入第{}阶的系数: ".format(i))))
        i = i + 1
    
    #n = 4
    #a = [50, -62, 39, 8, 1]    
    
    BairstowIteration(a)