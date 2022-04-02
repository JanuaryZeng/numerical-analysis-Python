import numpy as np

#Mat = np.array([[1.0,3,7,2],[5,1,2,1],[2,7,8,9]])
Mat = np.array([[1.0,2,3,4],[5,6,7,8],[9,1,2,3]])
#Mat = np.array([[1.,1.,2.],[ 1.,-1.,0.]])
def Gaussian(Mat):
    yLen = len(Mat)
    xLen = len(Mat[0])
    #将矩阵化为上三角增广矩阵，并返回此矩阵
    for i in range(yLen-1):
        maxium = 0
        temp = i
        for j in range(i,yLen):
            if Mat[j][i] > maxium:
                maxium = Mat[j][i]
                temp=j
        if temp!=i:
            for j in range(i,xLen):
                T = Mat[i][j]
                Mat[i][j] = Mat[temp][j]
                Mat[temp][j] = T
        for j in range(i+1,yLen):
            cz = Mat[j][i]/Mat[i][i]
            for k in range(i,xLen):
                Mat[j][k] = Mat[j][k] - cz*Mat[i][k]
    
    #对上三角增光矩阵进行求解
    #用于储存解
    X = np.zeros([yLen])
    for i in range(yLen-1,-1,-1):
        sumium = Mat[i][xLen-1]
        for j in range(i+1,xLen-1):
            sumium -= X[j]*Mat[i][j]
        X[i] = sumium/Mat[i][i]
    return X,Mat
boolean = int(input("输入1使用默认数据,输入其他数字手动输入数据：\n"))
if boolean!=1:
    n = int(input("请输入未知数个数："))
    Mat = np.zeros([n,n+1])
    for i in range(n):
        for j in range(n+1):
            Mat[i][j] = float(input("请输入第{}行，第{}列数据".format(i+1,j+1)))
print("原矩阵为：")
print(Mat)
X, Mat = Gaussian(Mat) 
print("上三角增广矩阵为：")
print(Mat)
print("解为：")
print(X)

"""
输入需要运算的增广矩阵
例如方程：
1*x1 + 3*x2 = 4
3*x1 + 5*x2 = 2
增广矩阵为：
[[1,3,4],[3,5,2]]
输入为下：

请输入未知数个数：2

请输入第0行，第0列数据1

请输入第0行，第1列数据3

请输入第0行，第2列数据4

请输入第1行，第0列数据3

请输入第1行，第1列数据5

请输入第1行，第2列数据2
"""