# Assignments 4
def Least_moves(x):
    if x==1:
        return 0
    elif x%2!=0:
        return 1+Least_moves(x-1)
    elif x%2==0:
        return 1+min(Least_moves(x-1),Least_moves(x/2))
print(Least_moves(5))
