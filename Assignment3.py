# Assignments 3
def Pascal_triangle(k):
    k=k-1
    line = [1]
    for i in range(max(k ,0)):
# 参考 https://www.pythonheidong.com/blog/article/613468/22f4e4748fe3d9445f36/
# pascal三角形中的n行k列的数为C_n^k
        line.append(int(line[i]*(k-i)/(i+1)))
    return line
print(Pascal_triangle(100))
print(Pascal_triangle(200))