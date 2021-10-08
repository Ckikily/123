#Assignment 2
#%%2.1
import numpy as np
M1=np.random.randint(1,50,size=(5,10))
M2=np.random.randint(1,50,size=(10,5))
#%%2.2
def Matrix_multip(A,B):
    # res_row=len(A)
    # res_col=len[B[0]]
    if len(A[0])==len(B):
        res = [[0] * len(B[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    res[i][j] += A[i][k] * B[k][j]
        return res
    return ('输入矩阵有误！')
#%%Result
Matrix_multip(M1,M2)