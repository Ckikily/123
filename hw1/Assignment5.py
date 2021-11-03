# # Assignments 5
#5.1
#运行5.1时需将5.2注释掉
numble1=[1,2,3,4,5,6,7,8,9]
numble=[8,7,6,5,4,3,2,1]
dp=[1,0,0,0,0,0,0,0,0]
num=[[0]*1 for _ in range(100)]
def Find_expression(k,dp1,jud,symbol=0,pre=9,cur=0,result=0):
    p=1
    if jud==1:
        p=p+1
    else:
        p=1
    if cur!=0: 
        dp1[9-cur]=symbol
    if result==k and cur>8:
        s=''
        count=0
        for i in dp1[1:]:
            if i==1:
                s=s+'%d'%numble1[count]+'+'
            elif i==-1:
                s=s+'%d'%numble1[count]+'-'
            elif i==0 :
                s=s+'%d'%numble1[count]
            count+=1
        s=s+'9=%d'%k
        print(s)
        num[k-1].append(1)
    elif cur>8:
        return 
    elif cur<8:
        Find_expression(k,dp1,0,1,numble[cur],cur+1,result+pre)
        Find_expression(k,dp1,0,-1,numble[cur],cur+1,result-pre)
        Find_expression(k,dp1,1,0,pre+(10**p)*numble[cur],cur+1,result)
    elif cur==8:
        Find_expression(k,dp1,0,1,0,cur+1,result+pre)
a=Find_expression(50,dp,0)
print(sum(num[50-1]))
#5.2
num1=[]
for i in range(1,101):
    Find_expression(i,dp,0)
for i in range(1,101):
    print("%d:%d种"%(i,sum(num[i-1])))
    num1.append(sum(num[i-1]))
num1.sort()
print(num1)
#50最多