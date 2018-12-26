import numpy as np
from scipy.linalg import inv

MatA = np.array([[1.0,2,3],[5,6,7],[9,1,2]])
MatB = np.array([4,8,3])

"""
函数名：LU
输入：系数A矩阵：MatA；B矩阵：MatB
输出：解：X
打印：L、U、D矩阵
"""
def LU(MatA,MatB):
    Len = len(MatA)
    L = np.zeros([Len,Len])
    U = np.zeros([Len,Len])
    D = np.zeros([Len,Len])
    X = np.zeros([Len,Len])
    
    #求出L U矩阵，并返回此矩阵
    for i in range(Len-1):
        maxium = 0
        temp = i
        for j in range(i,Len):
            if MatA[j][i] > maxium:
                maxium = MatA[j][i]
                temp=j
        if temp!=i:
            for j in range(i,Len):
                T = MatA[i][j]
                MatA[i][j] = MatA[temp][j]
                MatA[temp][j] = T
            T = MatB[i]
            MatB[i] = MatB[temp]
            MatB[temp] = T
        for j in range(i+1,Len):
            cz = MatA[j][i]/MatA[i][i]
            L[j][i] = cz
            for k in range(i,Len):
                MatA[j][k] = MatA[j][k] - cz*MatA[i][k]
    for i in range(Len):
        L[i][i] = 1
    
    U = MatA
#    assert inv(L)
    D = np.dot(inv(L),MatB)
#    assert inv(U)
    X = np.dot(inv(U),D)
    print("L矩阵为：")
    print(L)
    print("U矩阵为：")
    print(U)
    print("D矩阵为：")
    print(D)
    return X
    
    
boolean = int(input("输入1使用默认数据,输入其他数字手动输入数据：\n"))
if boolean!=1:
    n = int(input("请输入未知数个数："))
    print("输入系数矩阵A：")
    MatA = np.zeros([n,n])
    MatB = np.zeros([n])
    for i in range(n):
        for j in range(n):
            MatA[i][j] = float(input("请输入第{}行，第{}列数据".format(i+1,j+1)))
    print("请输入矩阵B:")
    for i in range(n):
        MatB[i] = float(input("请输入第{}个".format(i+1)))
    
print("系数A矩阵为：")
print(MatA)
print("矩阵B为：")
print(MatB)
X = LU(MatA,MatB) 
print("解为：")
print(X)
"""
需要分别输入系数A矩阵和B矩阵
例如方程：
1*x1 + 3*x2 = 4
3*x1 + 5*x2 = 2

系数A矩阵为：[[1,3],[3,5]]
B矩阵为：[[4,2]]

输入为下：

请输入未知数个数：2
输入系数矩阵A：

请输入第1行，第1列数据1

请输入第1行，第2列数据3

请输入第2行，第1列数据3

请输入第2行，第2列数据5
请输入矩阵B:

请输入第1个4

请输入第2个2

"""