a = int(input("请输入一个整数"))  
b = int(input("请输入一个整数"))  
c = int(input("请输入一个整数"))  
if a > b:
    if b > c:  
        print("{}>{}>{}".format(a, b, c))  
    elif b < c:  
        if a > c:  
            print("{}>{}>{}".format(a, c, b))  
        elif a < c:  
            print("{}>{}>{}".format(c, a, b))  
elif a < b:  
    if b < c:  
        print("{}>{}>{}".format(c, b, a))   
    elif c < b:  
            print(  ) 
